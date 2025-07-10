def read_log_file(filename):
    """로그 파일을 읽고 각 줄을 리스트로 반환한다."""
    log_entries = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    # 콤마로 나눠서 [날짜시간, 메시지] 리스트로 만든다
                    parts = line.split(',', 1)
                    if len(parts) == 2:
                        log_entries.append(parts)
    except FileNotFoundError:
        print(f'파일을 찾을 수 없습니다: {filename}')
    except Exception as e:
        print(f'오류 발생: {e}')
    return log_entries


def sort_log_entries(entries):
    """시간의 역순으로 로그를 정렬한다 (가장 최근 로그가 먼저 오도록)."""
    return sorted(entries, key=lambda x: x[0], reverse=True)


def convert_to_dict(entries):
    """리스트를 딕셔너리로 변환한다. 중복되는 키는 나중 로그가 덮어쓴다."""
    log_dict = {}
    for timestamp, message in entries:
        log_dict[timestamp] = message
    return log_dict


def save_to_json(data, filename):
    """딕셔너리를 JSON 포맷으로 파일에 저장한다."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write('{\n')
            count = 0
            total = len(data)
            for key, value in data.items():
                count += 1
                comma = ',' if count < total else ''
                file.write(f"  '{key}': '{value}'{comma}\n")
            file.write('}')
        print(f'{filename} 파일 저장 완료.')
    except Exception as e:
        print(f'파일 저장 중 오류 발생: {e}')


if __name__ == '__main__':
    filename = 'mission_computer_main.log'
    entries = read_log_file(filename)

    print('📄 원본 로그 리스트:')
    print(entries)

    sorted_entries = sort_log_entries(entries)
    print('\n⏳ 정렬된 로그 리스트:')
    print(sorted_entries)

    log_dict = convert_to_dict(sorted_entries)
    print('\n📚 딕셔너리 변환 결과:')
    print(log_dict)

    save_to_json(log_dict, 'mission_computer_main.json')

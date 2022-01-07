if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record = [name,score]
        records.append(record)
    
    second_lowest = sorted(list(set([score for name,score in records])))[1]
    result = [name for name,score in sorted(records) if score == second_lowest]
    
    for i in result :
        print(f"{i}")
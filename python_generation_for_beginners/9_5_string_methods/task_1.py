for i in range(1, int(input()) + 1):
    comment = input().strip()
    answer = comment if comment else "COMMENT SHOULD BE DELETED"
    print(f"{i}: {answer}")

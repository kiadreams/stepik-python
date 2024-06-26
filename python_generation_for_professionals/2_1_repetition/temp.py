def get_biggest(numbers: list) -> list:
    if not numbers:
        return [-1]
    else:
        # print(numbers)
        result = []
        for i in range(9, -1, -1):
            i_str = str(i)
            temp = [str(x) for x in numbers if str(x)[0] == i_str]
            # while temp:
            if not temp:
                continue
            m_len = len(max(temp, key=len))
            if i in [7]:
                pass
                # print(temp)
            temp.sort(
                key=lambda x: ((x * (m_len // len(x) + 1))[:m_len + 1]),
                reverse=True
            )
            if i in [7]:
                pass
                # print(temp)
            result.extend(temp)
        # return int(''.join(result))
        return result


a = ['7716', '7705', '7938', '7235', '7176', '7686', '7', '7451', '7012', '7009', '7697', '7298', '7497', '7778', '7795', '7919', '7608', '7882', '7718', '7827', '7947', '7826', '7139', '780', '7639', '7101', '72', '790', '7037', '7330', '7502', '7152', '7634', '7241', '7477', '7161', '7553', '7829', '7', '7604', '7955', '7212', '749', '7837', '7155', '7293', '7736', '776', '7119', '7523', '7360', '7839', '7295', '7887', '7254', '7763', '7743', '7293', 
'7042', '7230', '7831', '7822', '7311', '7496', '7675', '7805', '7005', '7607', '7569', '7466', '7850', '7220', '7646', '7030', '774', '7623', '7259', 
'7204', '7880', '7964', '7341', '7420', '737', '7480', '7203', '7663', '7092', '7717', '7862', '7388', '732', '7169', '750', '7165', '7637', '7062', '772', '7372', '7150', '7936', '7166', '7492', '7129', '7274', '7953']

right = ['7964', '7955', '7953', '7947', '7938', '7936', '7919', '790', '7887', '7882', '7880', '7862', '7850', '7839', '7837', '7831', '7829', '7827', '7826', '7822', '780', '7805', '7795', '7778', '7', '7', '776', '7763', '774', '7743', '7736', '772', '7718', '7717', '7716', '7705', '7697', '7686', '7675',
 '7663', '7646', '7639', '7637', '7634', '7623', '7608', '7607', '7604', '7569', '7553', '7523', '750', '7502', '7497', '749', '7496', '7492', '7480', '7477', '7466', '7451', '7420', '7388', '737', '7372', '7360', '7341', '7330', '732', '7311', '7298', '7295', '7293', '7293', '7274', '72', '7259', '7254', '7241', '7235', '7230', '7220', '7212', '7204', '7203', '7176', '7169', '7166', '7165', '7161', '7155', '7152', '7150', '7139', '7129', '7119', '7101', '7092', '7062', '7042', '7037', '7030', '7012', '7009', '7005']

b = [int(i) for i in a]
result = get_biggest(b)
answer = []
for i in range(len(result)):
    if result[i] != right[i]:
        answer.append((result[i], right[i]))
print(result == right)
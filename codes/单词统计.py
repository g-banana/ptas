#利用字典实现文本单词统计功能

def wordCount(input):
    words = input.split()
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

def difftext(tex1, tex2):
    lines1 = [line for line in tex1.splitlines() if line !='']
    lines2 = [line for line in tex2.splitlines() if line !='']
    lineNum = 0
    result = {}
    len1 = len(lines1)
    len2 = len(lines2)
    while lineNum < len1 or lineNum < len2:
        if lineNum >= len1:
            result[lineNum] = [None,lines2[lineNum]]
            lineNum += 1
            continue
        if lineNum >= len2:
            result[lineNum] = [lines1[lineNum],None]
            lineNum += 1
            continue
        if lines1[lineNum].split() != lines2[lineNum].split():
            result[lineNum] = [lines1[lineNum],lines2[lineNum]]
        lineNum += 1
    return result





tex1 = '''1
3

3'''
tex2 = '''1 2


3
4

24423423'''
difre = difftext(tex1,tex2)
print(difre)
def sanya_task():
    tmp = input('Введите последовательность целых чисел через пробел: ').split()
    if ',' in tmp:
        return 'Введите ЦЕЛЫЕ числа ЧЕРЕЗ ПРОБЕЛ'
    seq = list(map(int, input().split()))
    if len(tmp) < 2:
        return "Последовательность должна состоять как минимуи из 2х элементов"

    longest_seq, l_seq_coords = 0, []  # Определение переменных
    curr_seq, c_seq_coords = 0, []
    status = None

    for i in range(1, len(seq)):
        if seq[i] <= seq[i - 1]:  # Случай отрицательного роста
            if status != 'dcr':  # Случай, когда последовательность только стала отрицательной
                status = 'dcr'
                curr_seq = 2
                c_seq_coords = [i - 1, i]
            else:                 # Последовательность уже была отрицательной
                curr_seq += 1
                c_seq_coords[1] = i

        elif seq[i] > seq[i - 1]:  # Случай положительного роста
            if status != 'inc':  # Случай, когда последовательность только стала положительной
                status = 'inc'
                curr_seq = 2
                c_seq_coords = [i - 1, i]
            else:                 # Последовательность уже была положительной
                curr_seq += 1
                c_seq_coords[1] = i

        if curr_seq > longest_seq:
            longest_seq = curr_seq
            l_seq_coords = c_seq_coords

    ans = (f'Самая длинная монотонно изменяющаяся последовательность представляет собой срез: {l_seq_coords}\n'
           f'В представленной последовательности ее можно выделить, как: {", ".join(map(str, seq[:l_seq_coords[0]]))}'
           f' || {", ".join(map(str, seq[l_seq_coords[0]:l_seq_coords[1] + 1]))} || '
           f'{", ".join(map(str, seq[l_seq_coords[1] + 1:]))}')

    return ans


if __name__ == '__main__':
    print(sanya_task())

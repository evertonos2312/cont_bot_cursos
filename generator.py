import random


def generate_cpf(mask=False):
    cpf = [random.randint(0, 9) for x in range(9)]

    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11

        cpf.append(11 - val if val > 1 else 0)
    if mask:
        return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)
    else:
        return '%s%s%s%s%s%s%s%s%s%s%s' % tuple(cpf)


def generate_cnpj(mask=False):
    def calculate_special_digit(l):
        digit = 0

        for i, v in enumerate(l):
            digit += v * (i % 8 + 2)

        digit = 11 - digit % 11

        return digit if digit < 10 else 0

    cnpj = [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]

    for _ in range(2):
        cnpj = [calculate_special_digit(cnpj)] + cnpj

    if mask:
        return '%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(cnpj[::-1])
    else:
        return '%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % tuple(cnpj[::-1])


def random_number(digits):
    range_start = 10 ** (digits - 1)
    range_end = (10 ** digits) - 1
    return random.randint(range_start, range_end)


def gerenate_cep():
    def randomiza(n):
        return round(random.uniform(0, 1) * n)

    num_cep = 36
    cep1 = [0] * (num_cep + 1)
    cep1[0] = '86300000'
    cep1[1] = '86105000'
    cep1[2] = '16015244'
    cep1[3] = '60170001'
    cep1[4] = '28035042'
    cep1[5] = '71020631'
    cep1[6] = '03318000'
    cep1[7] = '30120060'
    cep1[8] = '01045001'
    cep1[9] = '68700216'
    cep1[10] = '88113350'
    cep1[11] = '13216000'
    cep1[12] = '62011140'
    cep1[13] = '30130005'
    cep1[14] = '06709015'
    cep1[15] = '04144070'
    cep1[16] = '29843000'
    cep1[17] = '95670000'
    cep1[18] = '64000290'
    cep1[19] = '59215000'
    cep1[20] = '04302021'
    cep1[21] = '29843000'
    cep1[22] = '04545005'
    cep1[23] = '64000290'
    cep1[24] = '20040002'
    cep1[25] = '66055260'
    cep1[26] = '79002290'
    cep1[27] = '75802095'
    cep1[28] = '96204040'
    cep1[29] = '76900032'
    cep1[30] = '80520560'
    cep1[31] = '05706777'
    cep1[32] = '86220000'
    cep1[33] = '29946490'
    cep1[34] = '09961660'
    cep1[35] = '14401150'
    cep1[36] = '03962040'

    return cep1[randomiza(num_cep)]




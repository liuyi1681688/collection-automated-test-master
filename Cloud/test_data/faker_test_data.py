from faker import Faker

# 创建和初始化一个生成器，可通过访问你想要的数据类型来命名的属性生成数据

# 选择中文
faker = Faker(locale="zh_CN")


class fakerTestData:

    # 随机生成姓名
    def get_name(self):
        # print(faker.name())
        return faker.name()

    # 随机生成手机号
    def get_phone_number(self):
        # print(faker.phone_number())
        return faker.phone_number()

    # 随机生成文字
    def get_text(self):
        # print(faker.text())
        return faker.text()

    # 随机词语
    def get_word(self):
        # print(faker.word())
        return faker.word()

    # 随机生成两位语言编码
    def get_language_code(self):
        # print(faker.language_code())
        return faker.language_code()

    # 随机生成字母
    def get_random_letter(self):
        random_letter = faker.random_letter() + faker.random_letter() + faker.random_letter()
        # print(random_letter)
        return random_letter


# 用于验证该脚本是否有效

# if __name__ == '__main__':
#     fd = fakerTestData()
#     fd.get_name()
#     fd.get_word()
#     fd.get_random_letter()
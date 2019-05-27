import allure


class Test_002:

    def test002(self):
        with open(r"C:\Users\James\Desktop\app8\scripts\chy.png", "rb") as f:
            allure.attach("图片", f.read(), allure.attach_type.PNG)

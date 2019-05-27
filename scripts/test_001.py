import allure,pytest

class Test_001:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是测试步骤1")
    def test001(self):
        print("--->test001")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是测试步骤2")
    def test002(self):
        print("--->test002")
        allure.attach("标题","具体描述信息")
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是测试步骤3")
    def test003(self):
        print("--->test003")
        allure.attach("标题", "具体描述信息")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是测试步骤4")
    def test004(self):
        print("--->test004")
        allure.attach("标题", "具体描述信息")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这是测试步骤5")
    def test005(self):
        print("--->test00")
        allure.attach("标题", "具体描述信息")
        assert True

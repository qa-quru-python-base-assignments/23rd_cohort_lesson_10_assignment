import allure
from selene import have, browser

repository_path = "/qa-quru-python-base-assignments/23rd_cohort_lesson_10_assignment"
expected_issue_title = "Test Issue"


@allure.epic("Репозитории")
@allure.feature("Issue")
@allure.story("Поиск Issue в репозитории")
@allure.tag("web")
@allure.severity(allure.severity_level.NORMAL)
@allure.link(f"https://github.com{repository_path}", name="Ссылка на репозиторий")
class TestGitHubIssue:

    # --- 1. Тест без шагов (Чистый Selene) ---
    @allure.title("Поиск Issue (без шагов)")
    @allure.description("Проверка существования Issue простым кодом без разметки шагов")
    def test_issue_search(self):
        browser.open(repository_path)
        browser.element("#issues-repo-tab-count").click()
        browser.element("[data-testid='issue-pr-title-link']").should(have.exact_text(expected_issue_title))

    # --- 2. Тест с динамическими шагами (Lambda Steps) ---
    @allure.title("Поиск Issue (с контекстными шагами)")
    @allure.description("Тест использует конструкцию 'with allure.step' для логирования действий внутри тела теста")
    def test_dynamic_steps_issue_search(self):
        with allure.step(f"Открыть репозиторий {repository_path}"):
            browser.open(repository_path)

        with allure.step("Перейти на вкладку Issues"):
            browser.element("#issues-repo-tab-count").click()

        with allure.step(f"Проверить наличие Issue с названием '{expected_issue_title}'"):
            browser.element("[data-testid='issue-pr-title-link']").should(have.exact_text(expected_issue_title))

    # --- 3. Тест с декораторами (Decorator Steps) ---
    @allure.title("Поиск Issue (с шагами-декораторами)")
    @allure.description("Тест использует переиспользуемые методы, помеченные декоратором @allure.step")
    def test_decorator_steps_issue_search(self):
        self.open_repository(repository_path)
        self.switch_to_issue_tab()
        self.assert_issue_title(expected_issue_title)

    @allure.step("Открыть репозиторий {path}")
    def open_repository(self, path: str):
        browser.open(path)

    @allure.step("Перейти на вкладку Issues")
    def switch_to_issue_tab(self):
        browser.element("#issues-repo-tab-count").click()

    @allure.step("Проверить наличие Issue с названием '{title}'")
    def assert_issue_title(self, title: str):
        browser.element("[data-testid='issue-pr-title-link']").should(have.exact_text(title))

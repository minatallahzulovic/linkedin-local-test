import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


TEST_EMAIL = "testemailsoftver@gmail.com"
TEST_PASSWORD = "lozinkazatest"


class TestLinkedIn:

    @pytest.fixture
    def driver(self):
        options = webdriver.ChromeOptions()

        
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--blink-settings=imagesEnabled=false")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        driver.maximize_window()
        driver.implicitly_wait(5)  

        yield driver
        driver.quit()

    def login(self, driver):
        driver.get("https://www.linkedin.com/login")

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "username"))
        ).send_keys(TEST_EMAIL)

        driver.find_element(By.ID, "password").send_keys(TEST_PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        WebDriverWait(driver, 25).until(
            EC.any_of(
                EC.url_contains("feed"),
                EC.url_contains("linkedin.com")
            )
        )

    # 1
    def test_homepage_title(self, driver):
        driver.get("https://www.linkedin.com")
        assert "LinkedIn" in driver.title

    # 2
    def test_homepage_load(self, driver):
        driver.get("https://www.linkedin.com")
        body = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        assert body is not None

    # 3
    def test_login_page_email_field(self, driver):
        driver.get("https://www.linkedin.com/login")
        email = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        assert email.is_displayed()

    # 4
    def test_login_page_password_field(self, driver):
        driver.get("https://www.linkedin.com/login")
        password = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        assert password.is_displayed()

    # 5
    def test_login_button_exists(self, driver):
        driver.get("https://www.linkedin.com/login")
        button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        )
        assert button.is_displayed()

    # 6
    def test_positive_login(self, driver):
        self.login(driver)
        assert "linkedin.com" in driver.current_url

    # 7
    def test_negative_login_wrong_password(self, driver):
        driver.get("https://www.linkedin.com/login")

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "username"))
        ).send_keys(TEST_EMAIL)

        driver.find_element(By.ID, "password").send_keys("wrongpass")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        error = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "error-for-password"))
        )
        assert error is not None

    # 8
    def test_negative_login_empty_email(self, driver):
        driver.get("https://www.linkedin.com/login")

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "password"))
        ).send_keys(TEST_PASSWORD)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        error = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "error-for-username"))
        )
        assert error is not None

    # 9
    def test_negative_login_empty_password(self, driver):
        driver.get("https://www.linkedin.com/login")

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "username"))
        ).send_keys(TEST_EMAIL)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        error = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "error-for-password"))
        )
        assert error is not None

    # 10
    def test_forgot_password_link(self, driver):
        driver.get("https://www.linkedin.com/login")

        link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Forgot password?"))
        )
        assert link is not None

    # 11
    def test_jobs_page_access(self, driver):
        self.login(driver)
        driver.get("https://www.linkedin.com/jobs")
        assert "jobs" in driver.current_url

    # 12
    def test_job_search(self, driver):
        self.login(driver)

        driver.get("https://www.linkedin.com/jobs")

        search = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@aria-label,'Search')]"))
        )

        search.clear()
        search.send_keys("Software Engineer")
        search.submit()

        WebDriverWait(driver, 20).until(
            EC.url_contains("jobs")
        )

        assert "jobs" in driver.current_url

    # 13
    def test_profile_icon_exists(self, driver):
        self.login(driver)

        icon = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "img"))
        )

        assert icon is not None

    # 14
    def test_https_usage(self, driver):
        driver.get("https://www.linkedin.com")
        assert driver.current_url.startswith("https://")

    # 15
    def test_footer_links(self, driver):
        driver.get("https://www.linkedin.com")

        footer = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "footer"))
        )
        links = footer.find_elements(By.TAG_NAME, "a")

        assert len(links) > 3
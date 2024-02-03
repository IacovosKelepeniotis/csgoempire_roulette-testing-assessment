import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def init_driver():
    # Construct the path to chromedriver
    driver_path = os.path.join(os.getcwd(), 'chromedriver-win64', 'chromedriver.exe')
    print(driver_path)  # Debug: Print the path to ensure it's correct

    # Create a Service object with the path to the ChromeDriver
    service = Service(executable_path=driver_path)

    # Initialize the Chrome driver with the service
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    return driver

driver = init_driver()

# Go to csgo roulette page
driver.get("https://csgoempire.com/roulette")

# Test: Validate Roulette Wheel Presence
def test_roulette_wheel_presence():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "wheel"))
    )
    print("Roulette wheel presence validated.")

# Test: Validate Rolling Number Visibility
def test_rolling_number_visibility():
    rolling_number = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".wheel__item .font-numeric"))
    )
    assert rolling_number.is_displayed(), "Rolling number is not visible"
    print(f"Rolling number visibility validated: {rolling_number.text}")



def test_bet_options_visibility():

    # Wait for the bet control buttons to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_any_elements_located((By.CSS_SELECTOR, ".bet-input__control"))
    )
    
    # Find all bet control buttons
    options = driver.find_elements(By.CSS_SELECTOR, ".bet-input__control")
    assert options, "Bet options are not visible"
    
    # Check for each bet option's visibility
    for option in options:
        assert option.is_displayed(), f"Bet option '{option.text}' is not visible"
        print(f"Bet option '{option.text}' is visible.")

def test_simulate_bet_placement():
    # Wait for the bet amount input field to be visible and then input a bet amount.
    bet_amount_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bet-input__field input[type='text']"))
    )
    bet_amount_field.clear()
    bet_amount_field.send_keys("100")  # Example bet amount

    # Wait for a short period to simulate user interaction delay and for the page to process the bet amount.
    WebDriverWait(driver, 2)

    # Assuming the bet buttons become enabled after setting a bet amount.
    # Trying to click the first available (enabled) bet button.
    try:
        bet_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".bet-btn:not(.bet-btn--disabled)"))
        )
        bet_button.click()
        print("Bet button clicked successfully.")
    except TimeoutException:
        print("Bet button did not become clickable. Test scenario may require adjustment based on actual page behavior.")
    except NoSuchElementException:
        print("No bet button found. Ensure the selector is correct and the element exists on the page.")



def test_ensure_bet_amounts_can_be_selected_or_inputted():
    
    
    # Assuming the bet amount field is present and selectable.
    bet_amount_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bet-input__field input[type='text']"))
    )
    bet_amount_field.clear()
    bet_amount_field.send_keys("100")  # Example bet amount
    
    # Verification: Check if the input field contains the correct amount
    assert bet_amount_field.get_attribute('value') == '100', "Bet amount not correctly inputted."
    
    print("Bet amounts can be selected or inputted successfully.")



def test_confirm_bet_buttons_are_clickable():
    # Wait for any condition that would enable the bet buttons. This might involve simulating other interactions.
    # For the sake of this example, we'll directly find buttons that are not disabled.
    enabled_bet_buttons = driver.find_elements(By.CSS_SELECTOR, ".bet-btn:not(.bet-btn--disabled)")
    
    for button in enabled_bet_buttons:
        assert button.is_enabled(), "Expected bet button to be enabled but it was not."
    
    if enabled_bet_buttons:
        print("Bet buttons are confirmed to be clickable.")
    else:
        print("No enabled bet buttons found. Test scenario may require adjustment.")


def test_verify_outcome_display_after_bet_simulation():

    # Simulate interactions leading up to a bet. As this needs to be login with money its an extra step
    # This involves setting a bet amount and selecting a bet option.
    # Here, I will assume these steps have been completed and check for a hypothetical outcome display element.
    
    # Placeholder: Wait for the outcome display to be visible. We will need to know the outcome of the for better understanding
    
    try:
        outcome_display = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".outcome-display-class"))  # Placeholder selector
        )
        print("Bet outcome displayed successfully.")
    except TimeoutException:
        print("Bet outcome not displayed. Check if simulation steps accurately reflect user interaction.")



test_roulette_wheel_presence()
test_rolling_number_visibility()
test_bet_options_visibility()
test_ensure_bet_amounts_can_be_selected_or_inputted()
test_confirm_bet_buttons_are_clickable()
test_verify_outcome_display_after_bet_simulation()

# Cleanup
driver.quit()


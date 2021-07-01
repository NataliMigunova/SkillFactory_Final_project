# List of test scenarious covered in the Project

## [Login and Logout functionality](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_login_logout_functionality.py)
Test suite for testing login/logout functionality for previously registered user in the system

- [Login](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_login_logout_functionality.py#L21)
  tests login functionality using credentials of already created user in advance
- [Logout](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_login_logout_functionality.py#L37)
  tests logout functionality for logged in customer
  
## [Website tabs functionality](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_tabs_verification.py)
Test suite which checks presence of all main menu tabs on the screen

- [Bestseller tab](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_tabs_verification.py#L17)
  tests that Bestseller tab opens and all related items are shown on the screen
- [New Items tab](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_tabs_verification.py#L25)
  tests that Latest tab opens and all related items are shown on the screen
- [For Her tab](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_tabs_verification.py#L33)
  tests that tab For Her opens and all related items are shown on the screen
- [For Him tab](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_tabs_verification.py#L41)
  tests that tab For Him opens and all related items are shown on the screen
- [For Kids tab](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_tabs_verification.py#L49)
  tests that tab For Kids opens and all related items are shown on the screen
- [For Home tab](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_tabs_verification.py#L57)
  tests that tab For Home opens and all related items are shown on the screen
- [Outlet tab](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_tabs_verification.py#L65)
  tests that tab Outlet opens and all related items are shown on the screen
- [Deals tab](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_tabs_verification.py#L73)
  tests that tab Deals opens and all related items are shown on the screen
- [Last Things tab](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_tabs_verification.py#L81)
  tests that tab Last Things opens and all related items are shown on the screen
  

## [Item Page functionality](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py)
Test suite which tests item info page has all expected components on it

- [Breadcrumbs test](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L18)
  tests that breadcrumbs shows current position according to website hierarchy
- [Description Header](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L28)
  tests that description header for opened item is presented on the screen
- [Item price](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L33)
  tests that price component is present on the screen
- [Color variants](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L38)
  tests that component with color selection for particular item is present on the screen
- [Size mesh component](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L43)
  tests that size mesh component is present on the screen
- [Add to cart button](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L48)
  tests that Add to Cart button is present on the screen
- [Add to favorite](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L53)
  tests that Add to favorite button is present on the screen
- [Return disclaimer](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L58)
  tests that return information disclaimer is actually on the screen
- [Return additional info](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L71)
  tests that additional return info is present on the screen after pressing button to show it
- [Precise Element Info](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L87)
  tests that element's precise info is present on the scree and represents additional information about an item
- [Information Block](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L93)
  tests that additional information block is actually on the screen
- [Alert disclaimer](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L104)
  tests that Alert Disclaimer is present on the screen and represents particular information
- [Review button](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L114)
  tests that review button is shown on the screen
- [Ask question block](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_item_page_information.py#L119)
  tests that Ask question block is present on the screen
  

## [Search item and Filter functionality](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py)
Test suite to test search functionality and filtering the objects
- [Search for proper item](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py#L16)
  tests that system can find items which are correctly represent any of the group of the items on the website
- [Incorrect item search](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py#L31)
  tests that information No Items Found shown when system was not able to find any result in search(incorrect group name)
- [Universal size filter](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py#L40)
  tests that Universal size items only shown when we click Universal size in size filter
- [XS size filter](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py#L43)
  tests that XS size items only shown when we click XS size in size filter
- [S size filter](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py#L46)
  tests that S size items only shown when we click S size in size filter
- [M size filter](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py#L49)
  tests that M size items only shown when we click M size in size filter
- [L size filter](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py#L52)
  tests that L size items only shown when we click L size in size filter  
- [XL size filter](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py#L55)
  tests that XL size items only shown when we click XL size in size filter  
- [Pink color filtering](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py#L59)
  tests that Pink color items are sorted after filter apply
- [Blue color filtering](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py#L62)
  tests that Blue color items are sorted after filter apply
- [Dark Blue color filtering](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py#L65)
  tests that Dark Blue color items are sorted after filter apply
- [Yellow color filtering](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py#L68)
  tests that Yellow color items are sorted after filter apply
- [Black color filtering](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/test_search_and_filter_functionality.py#L71)
  tests that Black color items are sorted after filter apply
  

## [Number of items on the screen switch functionality](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_Number_Of_Items_on_the_screen.py)
Test suite which changes number of shown items on the screen
- [Number of items on the screen is 90](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_Number_Of_Items_on_the_screen.py#L19)
  tests that default number of elements is 90
- [Number of items on the screen is 180](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_Number_Of_Items_on_the_screen.py#L24)
  switches to 180 items on the screen using select box
- [Number of items on the screen is 270](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_Number_Of_Items_on_the_screen.py#L30)
  switches to 270 items on the screen using select box
- [Number of items on the screen is 300](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_Number_Of_Items_on_the_screen.py#L36)
  switches to 300 items on the screen using select box
  

## [Sorting items on the screen functionality](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_Sorting_Of_Items_on_the_screen.py)
Test suite switches and tests sorting modes of items represented on the screen
- [Sorting alphabetical A-Z order](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_Sorting_Of_Items_on_the_screen.py)
  tests that items on the screen get sorted in alphabetical A-Z order
- [Sorting alphabetical Z-A order](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_Sorting_Of_Items_on_the_screen.py#L24)
  tests that items on the screen get sorted in alphabetical Z-A order
- [Sorting by price in low-high order](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_Sorting_Of_Items_on_the_screen.py#L31)
  tests that items on the screen get sorted by price from low to high amount
- [Sorting by price in high-low order](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_Sorting_Of_Items_on_the_screen.py#L38)
  tests that items on the screen get sorted by price from high to low amount
- [Sorting by date in low-high order](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_Sorting_Of_Items_on_the_screen.py#L45)
  tests that items on the screen get sorted by date from low to high
- [Sorting by date in high-low order](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_Sorting_Of_Items_on_the_screen.py#L51)
  tests that items on the screen get sorted by date from high to low
  

## [Cart functionality](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_cart_functionality.py)
Test suite which covers adding items to cart, removing and calculating total order info
- [Add item to cart](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_cart_functionality.py#L16)
  test adds an item to the cart, then checks that number of elements in the cart changed to 1 and checked that overall order amount is equal to item price
- [Add 2 items to cart](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_cart_functionality.py#L25)
  test adds 2 items to cart and verifies that number of element is 2 and total amount is equal to the sum of both items
- [Add item to cart and remove it](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_cart_functionality.py#L43)
  test adds 1 item to the cart, checks number of elements in the cart and total order amount, then removes the item and checks that the cart became empty with 0.0 amount in total
- [Recalculation of order summary](https://github.com/NataliMigunova/SkillFactory_Final_project/blob/master/Test_cart_functionality.py#L55)
  test adds 2 elements to the cart, verifies total order amount, then removes 1 element and verifies recalculated number of items and total order amount
  

## Possible scenarios not covered in tests
- Order submission functionality
- Add/edit/remove payment methods functionality
- Items return after order was submitted
- Order update after order was submitted
- Personal profile changes scenarios

These scenarios require additional effort and probably some test account to be used, because of real funds usage and verification on adding real payment methods

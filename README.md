# QA Engineer Test to Simetric

## Theory:

-   What are the limitations of Selenium testing?

    > -   It is primarily designed for web application testing and lacks robust support for testing desktop applications or mobile apps.
    > -   Writing tests that work reliably across different browsers can be challenging due to variations in CSS rendering, JavaScript execution, and browser-specific behaviors.
    > -   It can have a steep learning curve, especially for beginners.
    > -   It interacts with web browsers using JavaScript injection and DOM manipulation, which can introduce overhead and slower test execution compared to other testing frameworks
    > -   Itself does not provide built-in reporting capabilities or parallel test execution support.

-   What are the types of waits supported by WebDriver?

    > -   Implicit Waits
    > -   Explicit Waits
    > -   Fluent Waits

-   What is the major difference between driver.close() and driver.quit()

    > driver.close() is used to close the current window or tab, while driver.quit() is used to close all open windows/tabs and terminate the WebDriver session.

-   Can Captcha be automated?

    > The captchas are specifically designed to be difficult for automation tools to solve, including Selenium. Also the automated Captcha challenges is generally not feasible or reliable, even it can violate the terms of service of websites and can be considered unethical.

-   What does the switchTo() command do?

    > the switchTo() command is used to switch the focus or control to a different context within the web page. It allows you to navigate between different frames, windows, or pop-ups in order to interact with elements present.

-   When do we use findElement() and findElements()?

    > We can use findElement() when you want to locate a single element, and use findElements() when you want to locate multiple elements.

-   Explain how API testing differs from unit testing.

    > The unit testing primarily focuses on testing small, isolated units of code for correctness and reliability, while API testing focuses on testing the integration, communication, and behavior of APIs, involving multiple components or systems.

-   How do APIs work?

    > APIs facilitate communication between software systems by defining rules and protocols. Client applications send requests to API servers, which process the requests, generate responses, and send them back. The data is transmitted over the network using protocols like HTTP, and formats like JSON or XML. APIs enable seamless integration, data exchange, and access to functionality across applications.

-   What are the advantages of API Testing?

    > -   It allows for early detection of issues and defects in the functionality or behavior of APIs.
    > -   It provides a more efficient way to achieve comprehensive test coverage compared to UI testing.
    > -   API tests generally execute faster than UI tests since they don't involve rendering web pages or dealing with complex UI interactions.
    > -   API tests are less prone to breakage due to UI changes or cosmetic updates, as they focus on the underlying functionality rather than the user interface.
    > -   APIs play a crucial role in integrating different software systems and components.
    > -   It is highly amenable to automation, making it suitable for integration into continuous integration and delivery (CI/CD) pipelines.
    > -   PIs are often used to handle high volumes of data or concurrent requests.
    > -   APIs often involve authentication, authorization, and data security mechanisms

-   What are the advantages of UI Testing?

    > -   It allows you to simulate user interactions and validate the application's behavior from an end-user perspective.
    > -   It includes visual validation, where you can verify that the UI elements are rendered correctly, aligned properly, and visually consistent across different devices, browsers, and resolutions.
    > -   It allows you to simulate real-world scenarios by interacting with the application as an end user would.
    > -   It provides end-to-end testing capabilities by testing the entire application stack, including the UI, business logic, and back-end integrations.
    > -   It allows you to test the application in an environment similar to what users would experience.
    > -   It helps ensure that the application adheres to accessibility standards and guidelines.
    > -   It helps capture user feedback and satisfaction by identifying usability issues, design flaws, or user experience gaps.
    > -   It allows for comprehensive validation of the application's features, including form input validation, error handling, data integrity, and user feedback messages.

-   What is Latency in API testing?

    > The latency refers to the time delay or the amount of time it takes for a request to travel from the client to the server and for the corresponding response to travel back to the client. It measures the time elapsed between initiating a request and receiving the response.

-   List the most common status code that can response an API
    > -   200 OK
    > -   201 Created
    > -   204 No Content
    > -   400 Bad Request
    > -   401 Unauthorized
    > -   403 Forbidden
    > -   404 Not Found
    > -   500 Internal Server Error
    > -   503 Service Unavailable

## Practice:

-   Design and develop a script to find broken links in Selenium WebDriver
-   Implement a configuration to launch a test with Google Chrome and Firefox (do not necessarily have to run in parallel).
-   Create a test to validate the success response and the schema response of the next Python code:

```python
import requests
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.request("GET", url)
```

-   Implement a method to find elements into a webElement.
-   Taking as an example the html of the image, design a css selector to get the text of the h2 and p tag (marked with the red box)

**PD**: All scripts should be uploaded to a git project on GitHub on a public repository, preferably using Python as programming language.

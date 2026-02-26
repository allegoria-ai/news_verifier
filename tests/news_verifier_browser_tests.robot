*** Settings ***
Library    Browser

*** Variables ***
${NEWS_URL}    https://www.bbc.com/news

*** Test Cases ***
Open News Site And Check Title
    New Browser    chromium
    New Page    ${NEWS_URL}
    ${title}=    Get Title
    Should Contain    ${title}    BBC
    Close Browser


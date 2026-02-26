*** Settings ***
Library    OperatingSystem
Library    Collections
Library    JSONLibrary

*** Test Cases ***

News Results JSON Format Is Valid
    [Documentation]    Validate the structure and required fields of news_results.json
    ${json_path}=    Set Variable    news_results.json
    ${exists}=    Run Keyword And Return Status    File Should Exist    ${json_path}
    
    # Check alternative path if first fails
    IF    not ${exists}
        ${json_path}=    Set Variable    ../news_results.json
        File Should Exist    ${json_path}
    END

    ${json}=    Load JSON From File    ${json_path}
    Should Not Be Empty    ${json}

    FOR    ${item}    IN    @{json}
        # Validate Root Keys
        @{root_keys}=    Create List    rss_url    url    headline    headline_score    body_score    clickbait
        FOR    ${key}    IN    @{root_keys}
            Dictionary Should Contain Key    ${item}    ${key}
        END

        # Validate Nested headline_score
        ${h_score}=    Set Variable    ${item['headline_score']}
        Should Be True    isinstance($h_score, dict)
        Dictionary Should Contain Key    ${h_score}    neg
        Dictionary Should Contain Key    ${h_score}    neu
        Dictionary Should Contain Key    ${h_score}    pos
        Dictionary Should Contain Key    ${h_score}    compound

        # Validate Nested body_score
        ${b_score}=    Set Variable    ${item['body_score']}
        Should Be True    isinstance($b_score, dict)
        Dictionary Should Contain Key    ${b_score}    neg
        Dictionary Should Contain Key    ${b_score}    neu
        Dictionary Should Contain Key    ${b_score}    pos
        Dictionary Should Contain Key    ${b_score}    compound
    END

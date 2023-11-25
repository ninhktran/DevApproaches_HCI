# Data folder


## Idea behind this data process
When we started working on this project we were working in the data provided by the following paper: [How are diverse end-user human-centric issues discussed on GitHub?](https://dl.acm.org/doi/10.1145/3510458.3513014)

The dataset used is stored in the following path: data/Human-centric-issues-GitHub-552021.xlsx

## Process

In order to understand how the developers are fixing Human Centric Issues, we wanted to capture the following info:
- project_name: 
- issue_link: link to the issue, expect for the 2 apps mentioned above
- author: the person that started the initial issue thread
- body_text: text convo related to the issue

- project_name: the app that the issue is related to
- issue_link: github link to the github issue page
  - if there is no link available, we use the following placeholder: "github page for issue not found<br>issue#:{number}"
- issue_number: number of the issue
- author: 
- Issue_title: title of the issue
- issue_hci_attributes: 
- Created_At: creation date
- Issue_State: current status of the issue. It can have one of two values: open or closed
- State_Reason: The reason for the state change. Ignored unless state is changed. Can be one of: completed, not_planned, reopened, null
- closed_at: closing date
- body_summary: summary of the body text
- body_text: thread message captured on the original 
- English translation from German: some body texts are in german so we added this column 

Once this file was generated we, we manually went through every issue entry and checked whether it was fixed or not.<br>
If an issue was fixed we keep record what commits were linked to the fix, if any are available.

## Final result

At the end of this process, we have the following file *(still need to be added)*.

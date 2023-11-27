# Understanding Developers’ Approaches to Human-centric Issues in Mobile Apps: An Analysis of GitHub Data

## Citing this Work

If you use or refer to our work in your research or projects, we kindly ask you to cite our paper: *Understanding Developers’ Approaches to Human-centric Issues in Mobile Apps: An Analysis of GitHub Data*


## Overview
In the ever-evolving field of software engineering, mobile applications serve as an integral part of our digital ecosystem. Mobile applications often fails to meet diverse user needs, leading to accessibility and usability issues known as human-centric problems. These stem from overlooking users' characteristics and abilities during development. This project analyzes GitHub data to understand how developers address these issues.

## Motivation
Our research is driven by the need to understand how developers, especially in open-source projects, address Human-Computer Interaction (HCI) issues in mobile applications. We aim to uncover patterns and tactics used by developers to efficiently resolve HCI challenges, filling a knowledge gap in this area. By providing valuable insights, our research seeks to enhance software development, improve user experience, and contribute to building a more inclusive digital ecosystem.

## Related works
When we started working on this project we were working in the data provided by the following paper: [How are diverse end-user human-centric issues discussed on GitHub?](https://dl.acm.org/doi/10.1145/3510458.3513014) by Khalajzadeh, Hourieh et al. (DOI: 10.1145/3510458.3513014)

The result dataset of their work can be found here [https://zenodo.org/records/4739069](https://zenodo.org/records/4739069). We have stored it in our GitHub repository as: **Human-centric-issues-GitHub-552021.xlsx**


## Methodology

Our work was divided into 3 phases:
### Data Cleaning:
The research utilized data collected by [Khalajzadeh et al. (2022)](https://dl.acm.org/doi/10.1145/3510458.3513014), comprising 1244 issues from 6 apps. Issues with Human-Computer Interaction (HCI) problems were extracted using **dataParserInitial.py**, then supplemented with GitHub API data through the **dataParserFinal.py**. Then, we added summaries of each issue comment message using gpt-3.5-turbo. This resulted in **PostDataCleaning.xlsx** table. It has 216 issues, 164 of which are relevant since mobile-ios and mobile-android apps were excluded due to the unavailability of issue links.

### Issues Categorization:
The team employed open coding to categorize issues, collaborating on 40% and individually handling the remaining 60%. Discrepancies were resolved through discussion, resulting in 158 categorized issues across 7 different categories. The **postCategorization.xlsx** file contains the results of this phase.

### Code Fixes Categorization:
For code fixes, the team looked into the issues in the Closed and Merged category and categorized them into high-level categories. It is important to note that we only focused on issues that had commit related to them. Several issues were fixed through new releases and had no related commits, which meant we didn't look at them. A collaborative approach ensured consensus in categorization, leading to a comprehensive understanding of code fixes related to HCI issues. The *8IssueAndCommitCategorizations.xlsx** file contains the results of this phase. This spreadsheet contains our final results.


## Results
For more details on the results, please refer to our paper: *Understanding Developers’ Approaches to Human-centric Issues in Mobile Apps: An Analysis of GitHub Data*. But these sections represent our results at a high level.

### Issues Categorization
These are the issue categories:
- **Closed and Merged:** The issue was closed and fixed through code changes either through code commits or new releases
- **Closed as Duplicate:** The issue was reported but found to be a duplicate of another issue.
- **Closed as Won't Fix:** Developers acknowledged the issue but decided not to address it for specific reasons (e.g., low priority, technical limitations).
- **Closed as Works as Intended:** The reported behavior is the expected behavior, and no changes were made. The issue was due to misuse by the user.
- **Closed and Not Fixed:** The issue was reported, but developers closed it without resolving the problem.
- **Closed as out-of-scope:** Developers acknowledged the issue, but the fix depended on a third-party entity.
- **Closed with Workaround/Solution:** The issue was closed because a - solution was found that didn’t require a code change
- **Miscellaneous:** did not fit in any of the other categories.

This table represent the number of issues in each category in our applications
| Categories                     | healthchecks | firefox-ios | cwa-app-ios | cwa-app-android | Total |
|------------------------------- |--------------|-------------|-------------|-----------------|-------|
| Closed and Merged              | 18           | 30          | 24          | 13              | 85    |
| Closed as Duplicate            | 1            | 0           | 2           | 1               | 4     |
| Closed as Won't Fix            | 4            | 1           | 3           | 3               | 11    |
| Closed as Works as Intended    | 1            | 0           | 4           | 1               | 6     |
| Closed as out-of-scope         | 0            | 2           | 21          | 7               | 30    |
| Closed with Workaround/Solution| 4            | 4           | 5           | 0               | 13    |
| Miscellaneous                  | 1            | 2           | 2           | 4               | 9     |

### Code Fixes Categorization
These are the categories of code fixes:
- **Back-End Components:** Modifications to the server-side logic and code supporting the application functionality.
- **Data Handling:** Adjustments to data-related structures, processing, migration, and validation logic.
- **Documentation:** Updates made to the project documentation or file structure. 
- **Front-End Components:** Changes related to the visual and interactive aspects of the user interface.
- **Infrastructure and Deployment:** Updates to the application's hosting environment's setup, deployment, and configuration.
- **Internationalization and Localization:** Enhancements related to language support and locale-specific formats. 
- **Performance Optimization:** Code changes aimed at improving the application's speed, efficiency, and resource usage.
- **Security:** Commits to addressing vulnerability patches and changes following security-related matters.
- **Testing:** Modifications to testing code, including unit, integration, and end-to-end tests, as well as testing utilities.
- **User Interface Logic:** Changes to the logic managing user interface elements, state management, and navigation.

This table represents the number of HCI attributes in each code fix category
| Categories                           | Accessibility | Compatibility | Emotional aspects | Inclusiveness | Location/Language | Preference | Privacy/Security | Satisfaction | Total |
|------------------------------------- |---------------|---------------|-------------------|---------------|-------------------|------------|------------------|--------------|-------|
| Back-End Components                  | 0             | 0             | 0                 | 0             | 0                 | 1          | 0                | 1            | 2     |
| Data Handling                        | 0             | 0             | 0                 | 0             | 0                 | 1          | 0                | 1            | 2     |
| Documentation                        | 0             | 0             | 1                 | 1             | 2                 | 0          | 0                | 1            | 5     |
| Front-End Components                 | 5             | 0             | 0                 | 1             | 0                 | 1          | 0                | 1            | 8     |
| Infrastructure and Deployment        | 0             | 0             | 0                 | 0             | 0                 | 0          | 1                | 1            | 2     |
| Internationalization and Localization| 0             | 0             | 0                 | 0             | 1                 | 0          | 0                | 0            | 1     |
| Performance Optimization             | 0             | 0             | 0                 | 0             | 0                 | 0          | 0                | 1            | 1     |
| Security                             | 1             | 1             | 0                 | 0             | 0                 | 5          | 5                | 1            | 13    |
| Testing                              | 0             | 0             | 0                 | 0             | 0                 | 4          | 0                | 1            | 5     |
| User Interface Logic                 | 1             | 0             | 1                 | 0             | 0                 | 1          | 1                | 1            | 5     |

## Contributions
The main contributions of this work include:
- Developing an understanding of how human-centric issues are solved in open-source projects.
- Manual analysis of code-related fixes dealing with human-centric issues.
- Implications and possible future research directions to better manage human-centric issues in the software development process.

## Contact
This work was performed by a group of computer science graduate students at the University of Minnesota Twin-Cities as part of the following course CSCI8980: Automated Software Engineering

For questions or further information, feel free to contact
- [David Buyck](buyc0007@umn.edu)
- [Youssef Zahar](zahar022@umn.edu)
- [Ninh Tran](tran1108@umn.edu)

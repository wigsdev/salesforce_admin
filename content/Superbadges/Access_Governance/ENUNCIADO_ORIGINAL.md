# Superbadge: Access Governance

## Lo que tendrá que hacer para ganar esta Superbadge
*   Audit privileged users and adjust permissions appropriately.
*   Monitor changes to key data and mitigate exposure of sensitive data.

## Conceptos probados en esta Superbadge
*   Access Governance

---

## Prework and Notes

### Sign Up for a Developer Edition Org with Special Configuration
To complete this superbadge, you need a special Developer Edition org that contains special configuration and sample data. Note that this Developer Edition org is designed to work with the challenges in this superbadge.

1.  Sign up for a free Developer Edition org with special configuration.
2.  Fill out the form. For Email address, enter an active email address.
3.  After you fill out the form, click **Sign me up**.
4.  When you receive the activation email (this might take a few minutes), open it and click **Verify Account**.
5.  Complete your registration by setting your password and challenge question. 

> **Tip**: Save your username, password, and login URL in a secure place—such as a password manager—for easy access later.

You are logged in to your superbadge Developer Edition org.

**Now, connect your new Developer Edition org to Trailhead.**

1.  Make sure you’re logged in to your Trailhead account.
2.  In the Challenge section at the bottom of this page, select **Connect Org** from the picklist.
3.  On the login screen, enter the username and password for the Developer Edition org you just set up.
4.  On the **Allow Access?** page, click **Allow**.
5.  On the **Want to connect this org for hands-on challenges?** page, click **Yes! Save it**. You are redirected back to the Challenge page and ready to use your new Developer Edition org to earn this superbadge.

Now that you have a Salesforce org with special configuration for this superbadge, you’re good to go.

> **Note**: Before you begin the challenges, please review **Security Governance Superbadges: Trailhead Challenge Help**.

> **Important**: Make sure you’re using a new Developer Edition org from this sign up link to complete the challenges in this superbadge. If you use an org that has been used for other work, you won’t pass the challenges in this superbadge.

---

## Use Case
Strato-Form Generators has implemented security policies that include quarterly monitoring and auditing activities. While security is always top-of-mind for the org’s administrators, regular scans for potential security vulnerabilities help them keep the org in tip-top shape.

The Salesforce admins at Strato-Form Generators use a team approach to ensure adequate security monitoring. As an admin, you’ve been tasked with auditing users with privileged access and monitoring key data changes on opportunity records.

---

## Business Requirements
This section represents the requirements for your quarterly monitoring responsibilities and the actions you must take to make the org compliant with company policies.

### Audit Privileged Users

> **Note**: Developer Edition orgs allow only two active Salesforce users, including yourself. For this reason, most of the users in your org are set to inactive. You’ll need to review all users, active and inactive, in order to pass this challenge.

Strato-Form Generators adheres to the principle of least privilege to maintain a secure Salesforce org. This means that all users should only be given the minimum level of access required to do their jobs—nothing more. When it comes to elevated access and administrative privileges, it’s even more important to make sure access is granted to the right users and for the right amount of time.

But with many layers of permissions and org settings, it's possible to unintentionally grant privileged access or to allow continued access beyond the timeframe required.

Review the privileged access types and company policies below to remind yourself who should be granted certain access levels.

| Privileged Access Type | Company Policy |
| :--- | :--- |
| **Modify All Data** | Only system administrators |
| **View All Data** | Only system administrators<br><br>30-day temporary access for users with business justification and manager approval |
| **Customize Application** | Only system administrators<br><br>30-day temporary access for users with business justification and manager approval |
| **Manage Users** | Only system administrators |
| **Delete Opportunities** | Sales representatives: **NOT** authorized to delete opportunity records |

Now, scan your org to see who has privileged access and identify users who may need their access levels adjusted. For the purposes of this superbadge, your org has a couple of tools that may be helpful. The actions you take to identify users with privileged permissions will not be checked.

*   **Cases - Salesforce Ticket record type**: The admin team uses the Salesforce Ticket record type on the Case object to manage requests, including onboarding new users and changing access levels. The **Closed Salesforce Tickets** list view tracks past confirmation of approvals (if applicable) and the actions taken to complete the request.
*   **User Access and Permissions Assistant (Salesforce Labs package)**: This AppExchange app has been installed in your org. It gives admins the ability to analyze permissions and permission assignments.

> **Note**: Strato-Form Generators’ policy is to assign permissions in permission sets and permission set groups rather than at the profile level.

Once you’ve identified the two users whose permissions need adjusting, make the necessary changes to bring the user permissions back into compliance with company standards.

### Monitor Data Changes

> **Note**: The enhanced page layout editor interface presents accessibility challenges for screen readers attempting to modify object pages. For more information related to completing the challenge below, please review the Help article, Screen Reader Techniques for Adding Related Lists to Page Layouts.

A number of users at Strato-Form Generators have approached the admin team with questions about changes to opportunity records. Since the nature of the inquiries are generally centered around the same fields, you’ve recommended utilizing field history tracking for the following fields.

*   Close Date
*   Opportunity Owner
*   Stage
*   Amount

Make sure changes to these fields are tracked, and add the **Opportunity Field History** related list to the page for the **Opportunity Layout**.

Then, create a report to track recent changes to all opportunity records with the following requirements. Note: The User Access and Permissions Assistant app includes a Report tab that is different from the standard Reports object.

| Field/Filter | Value |
| :--- | :--- |
| **Report Name** | `Opp Field History - Last 7 Days` |
| **Report Unique Name** | `Opp_Field_History_Last_7_Days` |
| **Folder** | Compliance Reports |
| **Show Me** | All Opportunities |
| **Edit Date** | Last 7 Days |
| **Include** | Any |

Great work, your users love you! As you wrap up this field history activity, another high-priority field history task has landed on your desk.

A Strato-Form Generators user accidentally entered a client credit card number in the **Preferred Payment Method** field on the **Grand Hotels & Resorts Ltd** account. This field is not encrypted or protected appropriately to store sensitive account data. Luckily, the user realized their error quickly and deleted the number from the field. Phew! But you, the great admin that you are, know that field history tracking is enabled for that field, which means this sensitive data is still exposed.

You’re well aware that deleting field history is an action that shouldn’t be taken lightly. Your organization relies on field history to track important changes for auditing and compliance purposes. However, you also know that Strato-Form Generators has an obligation to its customers to protect their data. You notify your manager of the incident and you have received authorization to only delete the account history records that contain this sensitive information.

To complete this task, enable the deletion of field history for your org and assign yourself a temporary permission set that grants this authority to you. Make sure this permission is labeled `Delete Field History` with the API Name `Delete_Field_History` and a **1 day expiration date**.

Then, use a data import tool, like **Data Loader** or the free version of **dataloader.io**, to delete the records that contain the credit card number while maintaining all other account history records. We will not check the method you use to delete these records.

> **Note**: While it is a best practice to convert the Preferred Payment Method field from a text field to a picklist, that’s a task for another day. Take the rest of the day off, you #AwesomeAdmin you—you’ve earned it!

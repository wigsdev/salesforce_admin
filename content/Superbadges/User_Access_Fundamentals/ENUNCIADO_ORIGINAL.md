# Superbadge: User Access Fundamentals

### Lo que tendrá que hacer para ganar esta Superbadge
1.  Establish record access through organization-wide defaults.
2.  Create and modify profiles and their access.
3.  Manage access to standard and custom objects.
4.  Create permission sets and permission set groups.

### Conceptos probados en esta Superbadge
*   User Access

---

## Prework and Notes

1.  Create a new Trailhead Playground for this superbadge. Using this org for any other reason might create problems when validating the challenge.
2.  Complete all steps in this superbadge in Salesforce Lightning Experience.
3.  Some of the terminology used in this superbadge is descriptive and may not match the name as it appears in the user interface (UI). This is to test your knowledge of Salesforce features and ability to select the correct feature to satisfy a business need.
4.  Descriptions must be set for all new fields, permission sets, and so on in order to pass the challenges.

> **Note**: Before you begin the challenges, review User Access Superbadges: Trailhead Challenge Help.

---

## Use Case

Cloud Mouth Marketing (CMM) is a marketing firm that has recently seen its business take off. Over the last year, CMM has seen the demand for its services skyrocket, especially email marketing campaigns. While this has come as welcome growth for the crew at CMM, the volume of email has begun to exceed its internal capabilities. To help keep up with demand, CMM decides to enlist the help of ThunderMail, a third-party email marketing service.

As CMM’s Salesforce admin, it’s your responsibility to make sure the new email integration has just enough access to operate successfully.

---

## Business Requirements

This section represents the requirements for the integration user and object access.

### Marketing Integration User Setup

As a seasoned admin, you know the first step to giving ThunderMail access is to create a named user record and assign it a profile.

As a best practice, the admin team at CMM never grants more access than is necessary. Hello, principle of least privilege! For that reason, it has been determined that ThunderMail only requires minimum access to the Salesforce org to integrate successfully. To meet this requirement, find a standard profile that grants minimal access, and use this as a template for a new custom profile. Name this new profile `Marketing Email Integration User`.

With security always at the forefront, you make the smart decision to limit where user with the new integration profile can log in from. You’re able to obtain the IP address of ThunderMail’s secure server: `13.108.0.0`. Make sure that the integration user profile can only log in to your Salesforce org from this address.

With a new custom profile in place, all that’s left to do is create a named user record for the integration user. Make sure you generate a user record based on the requirements below.

*   **First Name**: Marketing Integration
*   **Last Name**: User
*   **Email**: `marketingintegrationuser@cloudmouth.com`
*   **Username**: Follow this formula: Add your initials and today’s date to the email address. Example: `marketingintegrationuser.KP090222@cloudmouth.com`
*   **User License**: Salesforce
*   **Profile**: Marketing Email Integration User
    *   *Note*: Make sure the username contains `marketingintegrationuser` in order to pass the challenge.

### Bulk Mail Custom Object

Based on the terms of the contract with ThunderMail, CMM will be charged based on total number of sends and recipients per month. Like any healthily skeptical admin, you recommend tracking the email sends in Salesforce in order to ensure accurate billing. To maintain an internal record of the email campaigns in your Salesforce org, create a new custom object with the Object name `Bulk Mail` (with API name `Bulk_Mail`) and the fields listed below.

In keeping with the industry best practices, and to allow for increased flexibility, you’ve decided to grant access to these fields via permission sets instead of profiles. These fields should only be visible to system administrators through field-level security. Don’t worry! You’ll set up permission sets later on to open visibility up to other users.

| Field Type | Field Name | Field API Name | Description |
| :--- | :--- | :--- | :--- |
| Text* | Subject | `Subject` | Subject of the email sent |
| Date/Time | Send Date | `Send_Date` | Date and time the email was sent |
| Number** | Number of Recipients | `Number_of_Recipients` | Total number of recipients for the email |

\* *Set the field length to 255 characters.*
\** *Leave the default settings for length and decimals.*

While the Bulk Mail object is built specifically to store data from ThunderMail, CMM believes in transparency where appropriate. Ensure that all users in your org are able to see, but not make changes to, Bulk Mail records.

### Marketing Integration User Access

Now that you’ve created the Bulk Mail object and the necessary fields, now you must make sure your users have the right access levels.

Because the integration user needs to have both Read and Write access to the Bulk Mail object, you decide it’s best to grant them this access separately from other users. Title your solution `Marketing Email Integration User` with the API name `Marketing_Email_Integration_User`.

To obtain all of the information necessary, the integration user needs access to several objects. Configure a solution that grants the following access.

| Object Permissions | Field Permissions \| Read Access | Field Permissions \| Edit Access |
| :--- | :--- | :--- |
| **Contact** | Read, Edit | Email, Lead Source | Email Opt Out |
| **Lead** | Read, Edit | Email, Lead Source | Email Opt Out |
| **Bulk Mail** | Read, Edit, Create | All fields | Number of Recipients, Send Date, Subject |

ThunderMail needs to make API requests to CMM’s Salesforce org in order to integrate successfully. Include the **API Enabled** permission in the `Marketing_Email_Integration_User` permission set. Finally, assign it to the Marketing Integration user.

### Additional User Access

> **Note**: Developer Edition orgs allow only two active Salesforce users, including yourself. For this reason, you don’t need to assign any of the permissions you configure for the challenge below.

Now that you have all of the necessary access granted to the Marketing Integration user, it’s time to focus on how other users can access the Bulk Mail object. Create a solution with the API name `Bulk_Mail_Read_Access`, and ensure that it provides users the ability to see, but not edit, all of the fields on the Bulk Mail custom object.

Once you’ve configured user access for the custom Bulk Mail object, you realize there are now a few permissions that apply to all users. Instead of assigning the permissions separately, you’d like to be able to assign them as a group. Create a new permission solution with the API name `All_Users` that bundles the following permissions.

*   Bulk Mail Read Access
*   CRM User
*   Standard Einstein Activity Capture
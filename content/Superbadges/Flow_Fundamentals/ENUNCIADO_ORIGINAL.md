# Superbadge: Flow Fundamentals

## What You'll Be Doing to Earn This Superbadge
*   Update existing flows to enhance automation.
*   Use flows to send emails, calculate values, and update records.

## Concepts Tested in This Superbadge
*   Configuring Action and Create Record elements
*   Using Resources and Flow Actions to save a record to a record variable
*   Using Get, Update, Decision, Assignment, and Loop elements in a flow
*   Creating a formula in a flow

## Note
We're hard at work bringing you updated superbadge content that reflects product enhancements and industry best practices. To complete this superbadge, you'll work with loops in flows, but we recommend checking out the transform element that is now available with flows, too. For more information, check out this Help documentation.

## Prework and Notes

### Sign Up for a Developer Edition Org with Special Configuration
To complete this superbadge, you need a special Developer Edition org that contains special configuration and sample data. Note that this Developer Edition org is designed to work with the challenges in this superbadge.

1.  Sign up for a free [Developer Edition org with special configuration](https://developer.salesforce.com/promotions/orgs/superbadge-flow-fundamentals).
2.  Fill out the form. For Email address, enter an active email address.
3.  After you fill out the form, click **Sign me up**.
4.  When you receive the activation email (this might take a few minutes), open it and click **Verify Account**.
5.  Complete your registration by setting your password and challenge question. **Tip:** Save your username, password, and login URL in a secure place—such as a password manager—for easy access later.
6.  You are logged in to your superbadge Developer Edition org.

### Now, connect your new Developer Edition org to Trailhead.
1.  Make sure you’re logged in to your Trailhead account.
2.  In the Challenge section at the bottom of this page, select **Connect Org** from the picklist.
3.  On the login screen, enter the username and password for the Developer Edition org you just set up.
4.  On the Allow Access? page, click **Allow**.
5.  On the Want to connect this org for hands-on challenges? page, click **Yes! Save it**. You are redirected back to the Challenge page and ready to use your new Developer Edition org to earn this superbadge.

Now that you have a Salesforce org with special configuration for this superbadge, you’re good to go.

### Tips
*   Enter all labels exactly as described in the instructions. Labels are case-sensitive and spelling counts.
*   When possible, copy and paste the label names from superbadge instructions instead of typing them.
*   If label names are not specified, you can use any name you choose; this applies to some Assignment elements and formulas.
*   Superbadges focus on very specific objectives; some best practices or typical approaches might not be required in the challenges.
*   Make sure you save your work before running the challenge check.
*   Ensure that you don’t create duplicate records, labels, permission sets, and so on, as part of any challenge.
*   Build your solution according to the requirements; adding more actions or steps can cause challenge checks to fail.

### Note
Before you begin the challenges, review **Flow Elements and Resources Superbadges: Trailhead Challenge Help**. Check out the accessibility section to learn more about screen reader and keyboard accessibility within Flow Builder.

If you’ve completed the **Superbadge: Flow Optimization** or the **Superbadge: Flow Administration**, you can use the same Developer Edition org to complete the challenges in this superbadge. If not, make sure you’re using a new Developer Edition org from this sign up link. If you use an org that’s been used for other work, you won’t pass the challenges in this superbadge.

## Use Case
**Dreamscape Bookshops** has flourished over the past few years for one reason: customer service. As a global network of local bookstores, Dreamscape has found a way to connect readers with new books they have likely never heard of. That’s because Dreamscape works with independent publishers and authors to identify new works readers will love. Its staff provides concierge-level engagement to connect readers with new works.

This innovative book-reader matching service is what helped Dreamscape grow, and personalized customer service has kept it growing. Dreamscape also has a loyalty program that it’s trying to maximize—to really give top-tier care to its most loyal readers.

Currently, each bookshop spends several hours a day carefully matching readers with new books. The shop teams then send emails to readers to let them know about new matches, events, and other fun happenings. As a longtime fan of Dreamscape Bookshops, you’re thrilled to be on the team that will help automate this process and save the staff a lot of time. Review Dreamscape’s automation requirements and identify ways to streamline their work. Then, sit back and enjoy new book recommendations!

## Business Requirements

### Book Order Giveaway
Personalized orders also keep loyal readers satisfied. An existing flow called **Book Order** helps the fulfillment team ensure books are quickly on their way, creating tasks for teams to spot-check book orders.

The team wants to add a new step to this process to add a free item to certain orders. Orders with three or more books should include a free bookmark, and orders with five or more books should receive a bookmark and sticker.

Adjust the existing flow called **Book Order** to create tasks relating to certain orders.

1.  Use a Decision element named `How Many Books in the Order?`.
2.  If the order has three or four books, create a task with subject `Add Bookmark`. Use the logic `Equals 3 OR 4` in the Decision element.
3.  If the order has five or more books, create a task with subject `Add Bookmark and Sticker` using the logic `Greater Than or Equal to 5`.
4.  Use the **Get Records for Queue** element to associate the tasks to the **Fulfillment Team queue**.
5.  Make sure the tasks are related to the current sale. **Tip:** Set the `OwnerId` and `WhatId` fields.
6.  Set the turnaround time to complete the task to 24 hours using a formula resource named `DueDate` for the `ActivityDate` field. Use the formula `{!$Flow.CurrentDate}+1`.

**Note:** It’s possible to configure this challenge in multiple ways, but for the sake of configuring your solution, configure it with multiple **Create Records** elements and no **Assignment** elements. You can test your automation with the flow called **Book Order**, available on the Contact record. As an optional confirmation of your work, use the flow to quickly create a Book Order record with book line items.

### Recommendation Email
Each week, the content team reviews a report of new books in the system and prepares quick summaries highlighting new books. The content team also reaches out individually to loyal readers with personalized recommendations. A custom field on the Book object called `Recommendation` allows the content team to describe how a new book might intrigue readers with certain interests. An existing formula field, `Why should you read this book?`, populates that information on the contact record.

A screen flow on the Contact record, **Recommendation Email**, should allow the content team to send an email to a reader from that reader’s Contact record after any updates they make. The previous admin left before this flow was finished.

1.  Adjust the **EmailBody Text Template** resource to include information about the book in the customer’s `Current Recommendation` field, including the title, author, and summary. Make sure the reader’s first name populates in the first line of the email.
2.  Ensure that the flow also updates the Contact record to add the date and time of this communication in the `Last Outreach` field.

**Note:** It’s possible to configure this challenge in multiple ways, but for the sake of configuring your solution, update the contact using the record variable from the **Get Records** element named `Get Customer Info`, and use a `$Flow` global variable for the date and time.

The existing flow is great, but confuses some of the team. Add a screen element to the **Recommendation Email** flow called `Confirmation Screen` with API name `Confirmation_Screen`. The new screen element should display the text `Your email has been sent`. The **Confirmation Screen** element should be the final element in the **Recommendation Email** flow.

**Tip:** You can test this flow to review your work; you must set the Automated Process User Email Address in the Process Automation Settings page to do so. We are not checking whether the flow is active or the related settings in this superbadge.

### Dreamscape Loyalty Program
Dreamscape readers are loyal readers. The loyalty program rewards readers for their purchases, online reviews, and more. The **Birthday Loyalty Points Update** flow sends an email to a reader on their birthday. A new feature of the loyalty program will be popular: free points assigned on the reader’s birthday!

| Level | Points Needed to Attain Level |
| :--- | :--- |
| **Gold** | 10,000 |
| **Silver** | 5,000 |
| **Bronze** | 2,000 |

Adjust the **Birthday Loyalty Points Update** flow to accommodate this change. Get the reader’s current loyalty status from the `Loyalty Status` field, and current points from the field `Loyalty Points` on the Contact record. Assign bonus birthday points based on the following:

*   **Gold**: 500
*   **Silver**: 250
*   **Bronze**: 100

Use the following logic in the flow to update the points value on Contact with special birthday points.

```sql
Case ({!Loop_Through_Contacts.Loyalty_Status__c},
    'Bronze',{!Loop_Through_Contacts.Loyalty_Points__c} +100,
    'Silver', {!Loop_Through_Contacts.Loyalty_Points__c} +250,
    'Gold', {!Loop_Through_Contacts.Loyalty_Points__c} +500,
    {!Loop_Through_Contacts.Loyalty_Points__c}
)
```

Wow, you’ve really improved automations for Dreamscape! Consider continuing on to the **Superbadge: Flow Optimization** to keep delivering so much additional functionality.
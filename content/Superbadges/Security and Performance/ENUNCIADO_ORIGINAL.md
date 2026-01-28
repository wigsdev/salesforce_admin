# Superbadge: Security and Performance

### Lo que tendrá que hacer para ganar esta Superbadge
*   Demonstrate how to use Big Objects for big data.
*   Work with external data.
*   Apply data classification, security, and access to fields.

### Conceptos probados en esta Superbadge
*   Big Objects
*   External Objects
*   Data Classification

---

## Prework and Notes

### Sign Up for a Developer Edition Org with Special Configuration
To complete this superbadge, you need a special Developer Edition org that contains special configuration and sample data. Note that this Developer Edition org is designed to work with the challenges in this superbadge.

1.  Sign up for a free Developer Edition org with special configuration.
2.  Fill out the form. For Email address, enter an active email address.
3.  After you fill out the form, click **Sign me up**.
4.  When you receive the activation email (this might take a few minutes), open it and click **Verify Account**.
5.  Complete your registration by setting your password and challenge question.
    *   **Tip**: Save your username, password, and login URL in a secure place—such as a password manager—for easy access later.
6.  You are logged in to your superbadge Developer Edition org.

**Now, connect your new Developer Edition org to Trailhead.**

1.  Make sure you’re logged in to your Trailhead account.
2.  In the Challenge section at the bottom of this page, select **Connect Org** from the picklist.
3.  On the login screen, enter the username and password for the Developer Edition org you just set up.
4.  On the **Allow Access?** page, click **Allow**.
5.  On the **Want to connect this org for hands-on challenges?** page, click **Yes! Save it**. You are redirected back to the Challenge page and ready to use your new Developer Edition org to earn this superbadge.

Now that you have a Salesforce org with special configuration for this superbadge, you’re good to go.



> **Note**
> *   Before you begin the challenges, please review Data Model Optimization Superbadges: Trailhead Challenge Help.
> *   Make sure you’re using a new Developer Edition org from this sign up link to complete the challenges in this superbadge. If you use an org that has been used for other work, you won’t pass the challenges in this superbadge.

Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms to avoid any effect on customer implementations.

### Tips
*   Grab a pen and paper. You may want to jot down notes and map out the data model as you read the requirements.
*   Enter all labels exactly as described in the instructions. Labels are case-sensitive and spelling counts.
*   When possible, copy and paste the label names from superbadge instructions instead of typing them.
*   Make sure you save your work before running the challenge check.
*   Build your solution according to the requirements; adding more configurations can cause challenge checks to fail.
*   We recommend following best practices and always including descriptions for configurations. However, we’re not checking for descriptions in this superbadge.

---

## Use Case

Flow and the Low Codes’s first album, *A Momentary Lapse of Memory*, has broken into the Top 10 on the Alt-Text Charts thanks to their new number-one hit song, “No More Mr. Wi-Fi.” But their success has been bolstered by a second hit song, “With or Without UI,” which has risen to number three in the charts.

As the quarter is coming to a close, the band’s manager, Art Tenor, wants to put together a way to track how many times a song is played on the two primary streaming platforms, Pineapple and Flowafy. Given the streaming success of both “No More Mr. Wi-Fi” and “With or Without UI,” the band is expected to have enough backing to produce their second album, *Back in Slack*, at Appy Road Studios.

While vinyl, CDs, and cassettes were the big-ticket sales back in the day, streaming platforms are now the number-one way that listeners consume music. And because listeners can play a song multiple times a day, the amount of data you collect will be enormous.

You need to think about a data model that can handle the volume of song plays.

### Standard Objects
The World Tour Manager app will use these standard objects.

*   **Account**: Venues for shows, vendors, streaming services, studios, and fans.
*   **Contact**: Fans, venue personnel, agents, producer, or manager.
*   **Campaign**: Tours (or groups of performances) by a particular band or a combination of bands (such as a music festival). Examples: World Tour, Errors Tour, and the Trailblazer Tour.
*   **Campaign member**: These are contact records related to a campaign.

### Custom Objects
As the Salesforce admin, you are responsible for maintaining the custom objects that interact with standard objects to keep track of all the elements that go into a tour. These custom objects represent details such as new songs, track lists, and even guest performers that can be updated and shared with stakeholders. The custom objects include:

*   **Song**: Includes fields such as Written by, Duration, Album, and so on.
*   **Album**: A collection of songs released together with band and production information, artwork, and bonus tracks.
*   **Track List**: A list of songs for a live show.
*   **Artist**: These are the singers, writers, and performers involved with the songs, albums, and even tours if it’s a guest artist performing with the band on a particular night.
*   **Performs On**: This object is used to connect Artists to Songs, in the future Art wants to be able to connect Artists to Albums too, however, that is out of scope for right now.

### Entity Relationship Diagram (ERD)
Review the current model in Schema Builder and diagram below to understand how the band is using standard and custom objects.

The entity relationship diagram shows the following relationships: The Account object has a master-detail relationship from the Contact object.
*   The Play Tracker object has required lookups with the Account and Song objects.
*   The Campaign object has a many-to-many relationship with the Campaign and Contact objects through the Campaign Member object.
*   The Campaign and Song objects have a many-to-many relationship with the Track List object.
*   The Song and Artist objects many-to-many relationships with the Performs On object.
*   The Account object has a lookup relationship from the Campaign object.
*   The Account object has a lookup relationship from the Contact object.
*   The Album object has a lookup relationship to the Song Object.

Downloadable PDF of the Entity Relationship Diagram (ERD).

---

## Business Requirements

### Support Song Play Tracking
Create a way to track song plays. The **Play TrackerCopiar** will have a number of required fields, including song, streaming service (**AccountCopiar**), number of plays, play date, start date for a tracking period, and end date for a tracking period. Other fields include device (such as a laptop, phone, or tablet), and operating system (such as iOS, Windows, or Android). Art Tenor informed you that when using the data in the object, the two most important fields, in order, are song and then streaming service (**AccountCopiar**). The fields should be in ascending order to improve query performance. He also points out that we should expect up to 500 rows of data per hour.

| Field Label | Field Purpose |
| :--- | :--- |
| SongCopiar | Connects Songs to Play Tracker |
| AccountCopiar | Connects Streaming Service (AccountCopiar) to Play Tracker |
| Number of PlaysCopiar | Holds the number of song plays |
| Play DateCopiar | Date that a song was played for that streaming service and device |
| Start DateCopiar | Start date/time of the tracking period for a song |
| End DateCopiar | End date/time of the tracking period for a song |
| DeviceCopiar | Device displays the type of device that the song was played on. Allocate for up to 60 characters. |
| OSCopiar | OS displays the operating system that the song was played on. Allocate for up to 60 characters. |

Once the Play Tracker is set up, you can check your work by loading in some data. (We won’t check this.)

| Start Date | End Date | Song | Streaming Service | Number of Plays | Play Date | Device | OS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2023-10-01 11:31:45 | 2023-10-31 11:31:45 | With or Without UI | Pineapple | 1,700,000 | 2023-10-27 00:00:00 | Phone | iOS |
| 2023-10-01 11:31:45 | 2023-10-31 11:31:45 | With or Without UI | Flowafy | 1,200,000 | 2023-10-27 00:00:00 | Phone | iOS |
| 2023-10-01 11:31:45 | 2023-10-31 11:31:45 | With or Without UI | Flowafy | 1,300,000 | 2023-10-27 00:00:00 | Tablet | iOS |
| 2023-10-01 11:31:45 | 2023-10-31 11:31:45 | With or Without UI | Pineapple | 1,600,000 | 2023-10-27 00:00:00 | Tablet | iOS |

### Bring in Ticket Sales Data
Flow and the Low Codes supports a charity organization called Save the DevOps. The band wants to donate 1,000 seats over several shows to the charity. In this challenge, you connect with the ticket vendor, TicketSnatcher, and check the band’s remaining tour dates at specific venues to determine the capacity, tickets sold, and tickets still available. Then create a report filtering capacity against tickets available to share with the band.

### Message from Developer Team

> We set up the required integration on the MuleSoft side. We’re now ready to hand over the guitar so you can connect to the integration we built and expose the performances (ticket sales) data from TicketSnatcher ticket vendor to Salesforce.

*   **Name**: PerformancesCopiar
*   **Request Row Counts** = false
*   **Performance data source URL**: `https://security-performance-33i1n3.5sc6y6-2.usa-e2.cloudhub.io/apiCopiar`
*   **Type**: Salesforce Connect: OData 4.0

Make sure to activate so we can rock and roll.

Once you have this setup, create a report named **Ticket TrackingCopiar** that includes all the fields. Create a folder named **Ticketing ReportsCopiar**. Save the report so that we can review the data.

### Enhance Fan Member Privacy
Fanny Loveflow is the new president of the official Flow and the Low Codes Fan Club. As president, she represents the band’s most devoted fans. Fans are granted early access to special material, exclusive music, concert tickets, VIP passes, rare merch, and virtual concerts. Fanny plays a crucial role in the band's community and advocates for the privacy and security of fan club members.

To access this content, Fanny and her team decide to issue each fan club member an 18-digit **Fan NumberCopiar** with enhanced security, include a description, and ensure that only Standard Users and System Administrators can see or edit the Fan Number. She also requests personal identifiable information (PII) for **EmailCopiar**, **BirthdateCopiar**, **Gender IdentityCopiar**, and **PronounsCopiar** are marked as confidential in the org.

Here's how the **Fan NumberCopiar** should look:

*   **Example Fan Number**: 13784-623-318-1989
*   **Displayed Fan Number**: XXXXXXXXXXXXXX1989
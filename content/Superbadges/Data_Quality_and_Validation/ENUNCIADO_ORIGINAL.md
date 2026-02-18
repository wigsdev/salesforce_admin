# Superbadge: Data Quality and Validation

## Lo que tendrá que hacer para ganar esta Superbadge

- Identify and address fields affected by data quality issues.
- Implement a solution to clean up and prevent duplicate contact records.
- Build validation rules to protect the quality of sales data.
- Enforce business processes with Flow.

## Conceptos puestos a prueba en esta Superbadge

- Data Quality
- Data Validation

---

## Prework and Notes

### Sign Up for a Developer Edition Org with Special Configuration

To complete this superbadge, you need a special Developer Edition org that contains special configuration and sample data. Note that this Developer Edition org is designed to work with the challenges in this superbadge.

1. Sign up for a free Developer Edition org with special configuration.
2. Fill out the form. For Email address, enter an active email address.
3. After you fill out the form, click **Sign me up**.
4. When you receive the activation email (this might take a few minutes), open it and click **Verify Account**.
5. Complete your registration by setting your password and challenge question. Tip: Save your username, password, and login URL in a secure place—such as a password manager—for easy access later.
6. You are logged in to your superbadge Developer Edition org.

**Now, connect your new Developer Edition org to Trailhead:**

1. Make sure you're logged in to your Trailhead account.
2. In the Challenge section at the bottom of this page, select **Connect Org** from the picklist.
3. On the login screen, enter the username and password for the Developer Edition org you just set up.
4. On the **Allow Access?** page, click **Allow**.
5. On the **Want to connect this org for hands-on challenges?** page, click **Yes! Save it.** You are redirected back to the Challenge page and ready to use your new Developer Edition org to earn this superbadge.

Now that you have a Salesforce org with special configuration for this superbadge, you're good to go.

> **Note**
> Before you begin the challenges, please review Data Quality and Validation Superbadge: Trailhead Challenge Help.
>
> Make sure you're using a new Developer Edition org from this sign up link to complete the challenges in this superbadge. If you use an org that has been used for other work, you won't pass the challenges in this superbadge.
>
> We recommend following best practices and always including descriptions when configuring validation rules, duplicate rules, and flow elements. However, we're not checking for descriptions unless specified in this superbadge.

---

## Use Case

Businesses need accurate data to thrive. In the age of AI, that's even more true. Data quality plays a crucial role in shaping the outcomes and reliability of AI systems because orgs rely on existing data to integrate AI agents and inform generative AI. In this superbadge, you demonstrate skills in data import, duplicate and validation rules, and data integrity maintenance using flows.

Working with the team at Cloud Kicks, you've heard plenty of puns about sneakers, but keeping things running smoothly as a Salesforce admin is a job you take seriously. Cloud Kicks makes stylish custom sneakers, and business never stands still. Really. Take the recent acquisition of trendy fashion retailer, Rambunctious Armadillo Socks (RAS). The RAS team brings high energy, creative ideas, and a lot of data into the mix. Your data management skills are needed to get the two CRM systems working together as one.

---

## Business Requirements

You've made initial steps to integrate RAS and Cloud Kicks data. But the business is experiencing data quality issues across Salesforce, due to inconsistent entry formats, duplicate records, and limited validation. This impacts reporting accuracy, user productivity, and the customer experience.

Your objective is to implement scalable and automated data quality solutions for the team at Cloud Kicks. In each challenge, you'll focus on specific areas of data, apply your expertise, and implement changes to ensure data quality. As a best practice, you've first verified that any planned updates won't trigger any automation in the org—such as flows, or Apex triggers—that could cause unintended side effects. With that confirmed, you're clear to proceed with improving the data.

---

## Challenge 1: Fix and Import Data

In your first challenge, help Cloud Kicks clean up some data that was imported from RAS into the **Lead Source Text** field. Your Data Quality Analysis dashboard includes many leads without a lead source. Use the **Lead Data Quality** report to review the affected leads.

The open text values have been saved to the `Lead Source Text` field on Lead records in the Cloud Kicks org. Your sales manager, José Figueroa, provided a table for the picklist mapping. It seems that RAS used an open text field on their website form, but Cloud Kicks uses a picklist. José has provided the lead source picklist value mapping here.

| Lead Source Picklist Values | Lead Source Text Values |
| :--- | :--- |
| Web | Website |
| Phone Inquiry | Call |
| | Phone |
| Partner Referral | RAS Referral |
| Purchased List | Tradeshow Scan |
| Other | SocialMedia |

Use this mapping and the **Lead Data Quality** report to import the proper value for the `Lead Source` picklist field on the RAS leads.

Nice job! You can open the **Data Quality Analysis** dashboard to examine the resulting changes and admire your work.

---

## Challenge 2: Manage Duplicates and Refine Rules

With the recent RAS acquisition, Cloud Kicks brought in a large volume of new customer data. Since the integration, there's been a noticeable spike in duplicate contact records within Salesforce. These duplicates are causing major inefficiencies. Sales Manager José has reported that sales reps are spending extra time sifting through multiple contact records to find the right one. Even more concerning, there have been a few cases where different reps have unknowingly contacted the same customer about the same opportunity, creating confusion and risking customer trust.

José asks you to take immediate action to control duplicates and clean up the contact records. You know that there's a duplicate rule named **Custom Contact Duplicate Rule** that's already configured in the org. Investigate why it isn't being triggered, and make the appropriate update. Configure the settings so that it will **block** users from creating duplicate contacts. Ensure the alert informs the user about a duplicate, and prompts them to use the existing contact record instead. Leave the report checkbox enabled for edit.

You check the logic used to identify duplicates in the **Custom Contact Matching Rule**. You're satisfied with the settings for an exact match on both email and last name. However, since valid first names can vary quite a bit, you decide to add a first name rule to allow for **approximate matches**.

Finally, use the **Duplicate Record Set Report** to find and merge duplicate records.

---

## Challenge 3: Enhance Data Validation for Opportunities

As Cloud Kicks matures its sales process, the Sales Ops department is focused on tightening forecast accuracy and improving the integrity of sales timelines. They've alerted you that sales reps are occasionally changing the opportunity stage on closed opportunities, either by mistake or in an attempt to "revive" deals that were already closed.

1. Create a validation rule named `Opportunity_Closed_Stages` and add a formula that **prevents changing the Stage** when it is set to **Closed Won** or **Closed Lost**. Make sure the user sees a relevant error message at the top of the page explaining why they can't change the opportunity stage once the stage is set to Closed Won or Closed Lost.

2. Create a validation rule named `Opportunity_Closed_Backdate` that **prevents users from entering a Close Date prior to today**. Be sure to include a relevant error message on the field that explains why they can't save the record. To maintain flexibility, make sure the validation rule is bypassed if the running user has the **Opportunity Manager** custom permission that already exists in the org.

3. Create a validation rule named `Opportunity_Amount_Owner_or_Admin` that ensures the opportunity **Amount can't be changed by anyone except an administrator or the record owner**. Make sure the user sees an error message on the Amount field specifying who can change the amount.

---

## Challenge 4: Enforce Task Due Date Constraints with Flows

People are bursting with enthusiasm about the stylish, comfortable footwear at Cloud Kicks. Fashion-forward input from the RAS team has energized the creative group with some fresh, innovative designs. Sales reps are entering more deals than ever into the pipeline. Keen to keep up with new business, the order processing and deliveries teams are automating more tasks than ever before.

Unfortunately, support agents have sometimes created follow-up tasks on high-priority cases with a due date past the case service level agreement (SLA), leading to inefficiencies, errors, and flawed insights. Time to apply your high-quality standards for data management to help structure workflows. Configure a flow to keep cases on track and establish rules for timely follow-up tasks. **Ensure that tasks on high-priority cases are created with a due date no more than 7 days out.**

Create a new flow with:
- **Label**: `Task Due Date`
- **API Name**: `Task_Due_Date`
- Runs when a **new task is created**.

### Flow Elements Required

| Element | Label | API Name |
| :--- | :--- | :--- |
| Get Records | `Get High Priority Cases` | `Get_High_Priority_Cases` |
| Decision | `Any High Priority Cases?` | `Any_High_Priority_Cases` |
| → Outcome (Yes) | `Yes - High Priority Found` | *(auto)* |
| → Outcome (Default) | *(leave default)* | *(auto)* |
| Decision | `Is The ActivityDate Too Far Into The Future?` | `Is_The_ActivityDate_Too_Far_Into_The_Future` |
| → Outcome (Yes) | `Yes - Too Far Into The Future` | *(auto)* |
| → Outcome (Default) | *(leave default)* | *(auto)* |
| Custom Error | `Error - ActivityDate Should Be Sooner` | `Error_ActivityDate_Should_Be_Sooner` |

**Get Records element**: Query for the related open cases and check if `Priority = High`.

**Formula**: Create a formula named `OneWeek` to determine if the task's due date is set more than 7 days out.

**Error message**: `High Priority cases need to be addressed quickly. Please set the due date no later than {!OneWeek}`. Show the error as an **inline error on the field Due Date Only**.

> Be sure to add a description to the error element (exact text not checked).

Your flow solution should incorporate clear logic while preventing scheduling conflicts for critical tasks. Nice work, Trailblazer!

---

## Sum It Up

By completing this superbadge, you've showcased your proficiency in data management. You were able to improve lead data quality after analyzing a report, mapping missing fields, and correcting inaccurate data. You identified and resolved duplicate contacts in the Cloud Kicks org, and refined rules to improve duplicate detection and block duplicate creation. You implemented new validation measures to secure opportunity data and accurate date fields. And in your final challenge, you incorporated flow automation, formula fields, and lookup filters to ensure data consistency across high-priority cases. Congratulations on this superbadge accomplishment!
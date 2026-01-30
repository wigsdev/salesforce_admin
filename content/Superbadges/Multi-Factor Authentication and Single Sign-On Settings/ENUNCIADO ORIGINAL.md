# Superbadge: Multi-Factor Authentication and Single Sign-On Settings

## Lo que tendrá que hacer para ganar esta Superbadge
* Configure single sign-on settings.
* Set up multi-factor authentication.
* Enable Lightning Login.
* Test configurations with the Salesforce Authenticator app.

## Conceptos probados en esta Superbadge
* User Authentication

## Prework and Notes

### Sign Up for a Developer Edition Org with Special Configuration
To complete this superbadge, you need a special Developer Edition org that contains special configuration and sample data. Note that this Developer Edition org is designed to work with the challenges in this superbadge.

1. Sign up for a free Developer Edition org with special configuration.
2. Fill out the form. For Email address, enter an active email address.
3. After you fill out the form, click **Sign me up**.
4. When you receive the activation email (this might take a few minutes), open it and click **Verify Account**.
5. Complete your registration by setting your password and challenge question. 
    * **Tip:** Save your username, password, and login URL in a secure place—such as a password manager—for easy access later.

You are logged in to your superbadge Developer Edition org.

Now, connect your new Developer Edition org to Trailhead.

1. Make sure you’re logged in to your Trailhead account.
2. In the Challenge section at the bottom of this page, select **Connect Org** from the picklist.
3. On the login screen, enter the username and password for the Developer Edition org you just set up.
4. On the **Allow Access?** page, click **Allow**.
5. On the **Want to connect this org for hands-on challenges?** page, click **Yes! Save it**. You are redirected back to the Challenge page and ready to use your new Developer Edition org to earn this superbadge.

Now that you have a Salesforce org with special configuration for this superbadge, you’re good to go.

### Note
Before you begin the challenges, please review **User Authentication Superbadges: Trailhead Challenge Help**.

**Make sure you’re using a new Developer Edition org from this sign up link to complete the challenges in this superbadge.** If you use an org that’s been used for other work, you won’t pass the challenges in this superbadge.

## Use Case
Cumulus Global Bank is growing rapidly and recently acquired Cirrus Cash Flow. Business leaders have identified the need for a new Salesforce org to house their customer service operations.

As a premier Salesforce security consultant, you’ve been tasked with implementing single sign-on (SSO) and multi-factor authentication (MFA) for the new customer service org. You’ve met with key stakeholders and compiled a comprehensive set of authentication requirements.

## Business Requirements
This section represents the culmination of many meetings and will be the basis of your work to transform the new org into a cloud-based version of the Louvre—authorized individuals only!

### Test Users
Two test users have been provided in your special org for this superbadge.

* **Murphy Jean:** SSO Testing
* **Brochan Pane:** “Break Glass” administrator Testing

You need to log in as these users in later challenges, so be sure to change their emails to your email address and generate new passwords for later access. 
* **Tip:** Use an Incognito browser when logging in as these users. Otherwise, be sure to log out and reauthenticate as your admin user before you make additional configurations.

**Important:** Do not change the usernames set for these users.

### Single Sign-On
Due to the evolving threat landscape, Cumulus Global Bank wants to streamline enhanced security protocols so it can control user access for all applications in one place. You’ve been asked to implement SSO for the company’s new Salesforce org so that all users are required to log in with SSO using their Federation IDs.

First, you need to make sure that users cannot log in to the org with their Salesforce credentials. Create a permission set called `Single Sign-On` with an API name of `Single_Sign_On` for this requirement, and use Murphy Jean as the SSO test user. Be sure to set a Federation ID for this user as you’ll need it in later steps. Use whatever value you’d like for Federation ID.

Next, configure inbound SSO. In this step, you’ll use the Axiom Heroku web app as the identity provider (IdP). Axiom has provided you with the following Security Assertion Markup Language (SAML) settings for the Salesforce configuration.

| Field | Value |
| :--- | :--- |
| Name | Axiom SSO Test |
| API Name | Axiom_SSO_Test |
| Issuer | `https://axiomsso.herokuapp.com` |
| Identity Provider Certificate | Download the Identity Provider Certificate from Axiom, then upload in this field. |
| Request Signature Method | RSA-SHA1 |
| SAML Identity Type | Federation ID |
| Identity Provider Login URL | `https://axiomsso.herokuapp.com/RequestSamlResponse.action` |
| Entity ID | `<The org’s My Domain URL>` |

**Note:** If a setting is not listed here, leave the default setting as is.

Now that you have SSO enabled and set up in the Salesforce org, test your configuration by generating a SAML response from the Axiom Heroku web app. A successful test allows you to log in to the org via SSO as the Murphy Jean user.
* The Axiom SAML version must match the version in your SAML SSO Settings.
* Set the Recipient URL to the Login URL endpoint.

Finally, make sure that users are unable to bypass the SSO requirement by preventing direct login from `login.salesforce.com`. And, since you always have user experience in mind, add a button to the org’s My Domain login page that takes users directly to the Axiom SSO Test authentication service. 
* **Note:** We won’t check for the SSO button, but adding it is best practice.

**Important:** Don’t lock yourself out of your org for this superbadge!

1. Make note of the org’s My Domain URL. You may need it for future access.
2. Do not uncheck the Login Form authentication service.

As a seasoned Salesforce consultant, you’re well aware that MFA is required for all users as of February 2022. Cumulus Global Bank has decided that the MFA requirement will be completed through the SSO IdP, so it doesn’t need to be configured within Salesforce for SSO users.

### Break Glass Administrator Configurations
In the event of an outage with the SSO IdP, the Break Glass admin needs to maintain access to the org. This user will generally log in with SSO like the rest of the org’s users, but they need the ability to log in from the org’s My Domain URL. The team at Cumulus Global Bank has emphasized that security is a top priority for the select few with the Break Glass Administrator profile.

Use the Brochan Pane user provided in your special org to test the configurations described below.

### Multi-Factor Authentication
The Break Glass user is required to pass a MFA verification challenge. Use a permission set labeled `MFA Authorization for Break Glass Admin` with the API Name `MFA_Authorization_for_Break_Glass_Admin` for this requirement.

### Lightning Login
Enable Lightning Login to add an extra layer of security and to streamline the Break Glass admin login procedure. Make sure that only users with the permission set labeled `Lightning Login User` (API Name `Lightning_Login_User`) can log in with this method.

### Salesforce Authenticator App
Log in as Brochan Pane to connect the Salesforce Authenticator app, enroll in Lightning Login, and test the configurations you made above. Don’t use the Axiom IdP to log in as this user.

**Note:** If you already have the Salesforce Authenticator app installed on your mobile device, you can simply add Brochan Pane’s account for testing.

---

## ¿Listo para superar esta Superbadge?
Realizará el trabajo para esta Superbadge en su propia organización de prácticas. Cada Superbadge tiene requisitos, configuraciones, licencias y restricciones de organización exclusivos. Siga los pasos de la sección Trabajo previo y Notas cuidadosamente para configurar una nueva organización para esta Superbadge; esto podría llevar aparejado instalar un paquete en un nuevo Trailhead Playground o registrarse para una organización de Developer Edition especial.

Para trabajar con su Trailhead Playground, haga clic en Launch (Iniciar). Para crear una organización de Developer Edition especial, siga los pasos en Prework (Trabajo previo) y Notes (Notas).

### Seleccionar organización de prácticas
* wilmergulcochia6@idea.com
* Creado el 30/1/2026

## Complete each challenge to earn your superbadge

### 1. Single Sign-On User Configurations
Make the appropriate configurations to set up Murphy Jean as your SSO test user.

### 2. SAML Configurations and Testing
Configure the SAML SSO Settings appropriately, and test your configuration using the Axiom IdP.

**Important:** Save your org's My Domain URL before moving on. You'll no longer be able to log in from `login.salesforce.com`.

### 3. Multi-Factor Authentication
Configure MFA for the Break Glass admin user.
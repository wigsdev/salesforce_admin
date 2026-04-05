Superbadge: Agentforce Service
Lo que tendrá que hacer para ganar esta Superbadge
Set up Agentforce Data Library.
Configure Service Agent.
Build and test custom agent actions.
Add and configure standard and custom topics.
Set up routing and escalation flows.
Conceptos puestos a prueba en esta Superbadge
Service Agent Configuration
Agentforce Data Library
Custom and Standard Topics
Agent Actions
Conversation Routing

Update
Thank you for your patience while a product issue temporarily impacted completion of this superbadge. We're happy to report that the Knowledge article retriever issue has now been resolved.

If you have an existing org that was blocked on Challenge 3 due to this issue, you can try to delete the existing Knowledge data library and then re-create it with the same label, waiting for the Status to become In Progress or Ready before building Challenge 3. If you still experience errors, we recommend starting over with a fresh org from the signup page and using that to complete the challenges. (Note that if you've already passed Challenges 1 and 2, you'll only need to rebuild Challenge 1 in your new org before building and passing Challenge 3, but please note that this could impact the functionality of your agent.) We apologize for the inconvenience.


Introduction to Superbadges
Heads-up! A superbadge is different from other learning on Trailhead. It's a hands-on technical skills assessment where you take business requirements and apply your skills to build something amazing, without the step-by-step guidance. We have provided recommended learning and Help articles filled with resources to aid you along your journey. The estimated completion time assumes prior experience with the superbadge concepts and completion of the recommended learning. Your hard work will pay off!

Prework and Notes
Sign Up for a Developer Edition Org with Special Configuration
To complete this superbadge, you need a special Developer Edition org that contains special configuration and sample data. Note that this Developer Edition org is designed to work with the challenges in this superbadge.

Sign up for a free 4-day Developer Edition org with special configuration and Data 360.

Fill out the form. For Email address, enter an active email address where you can receive the email confirmation for the new account.

After you fill out the form, click Submit. A confirmation message appears.
When you receive the activation email (this might take up to an hour), open it and click the link to reset your password.

Complete your registration by setting your password and challenge question. Tip: Save your username, password, and login URL in a secure place—such as a password manager—for easy access later.

You're logged in to your superbadge Developer Edition org.

Now, connect your new Developer Edition org to Trailhead.

Make sure you’re logged in to your Trailhead account.

In the Challenge section at the bottom of this page, select Connect Org from the picklist.

On the login screen, enter the username and password for the Developer Edition org you just set up.

On the Allow Access? page, click Allow.

On the Want to connect this org for hands-on challenges? page, click Yes! Save it. You're redirected back to the Challenge page and ready to use your new Developer Edition org to earn this superbadge.

Now that you have a Salesforce org with special configuration for this superbadge, you’re good to go.

This superbadge requires access to a special Developer Edition org that includes Einstein Generative AI and Data 360. These Developer Edition orgs are only available for a 4-day period, so be sure to complete this superbadge before your org expires.



Note
Before you begin the challenges, review Agentforce Service Superbadge: Trailhead Challenge Help.

Make sure you’re using a new Developer Edition org from this sign up link to complete the challenges in this superbadge. If you use an org that has been used for other work, you won’t pass the challenges in this superbadge.

Use Case
Coral Cloud Resorts, a luxury seaside destination, is well-known for its seasonal offerings and dedication to providing personalized, high-quality guest experiences. Typically, the resort has its busiest season in the summer, with quieter off-season months. However, this year, the resort faces an exciting but complex challenge: An independent film festival is being hosted nearby during the off-season. This event is expected to draw a large volume of new and returning guests.

Adding to the excitement, Coral Cloud Resorts is to host several exclusive festival meet-and-greet events onsite. These high-profile activities, combined with increased guest demand, create unique operational pressures for the resort.

To meet these demands, Coral Cloud Resorts is expanding service hours, offering exclusive film festival-related activities, and rolling out new event options—all while maintaining high standards of guest service. To achieve this without significantly increasing staffing, the resort is turning to automation and artificial intelligence (AI)-driven customer service solutions.

Business Requirements
The Coral Cloud Experience Agent acts as a virtual concierge, handling guest inquiries and assisting with bookings, festival recommendations, and other services. Your task is to configure and optimize the agent to meet the following business needs.

Set up the Coral Cloud Experience Agent: Configure the agent to deliver personalized, accurate responses using trusted data sources like the Agentforce Data Library and Knowledge articles.
Manage bookings efficiently: Equip the agent with actions to modify guest bookings, such as adding or canceling reservations, and provide real-time booking information.
Expand service with standard and custom topics: Use topics like General FAQs to handle common questions and create custom topics to highlight festival-related offerings.
Handle complex queries with escalations: Set up routing flows to transfer unresolved or complex guest queries to service representatives for further assistance.
With your configuration expertise, the Coral Cloud Experience Agent can help the resort maintain exceptional guest service during the busy festival season while optimizing staff workloads.

Set Up the Agent and Agentforce Data Library
Configure the agent and set up data libraries to deliver accurate and consistent responses. The org already has an Agentforce Service Agent called Coral Cloud Experience Agent.

Turn on Einstein and Agentforce if they aren't already enabled.

Define the Agent’s Role and Context
Field	Value
Description	This is Coral Cloud Resorts' AI agent, designed to help customers discover resort experiences and book sessions seamlessly, particularly during the film festival.Copiar
Role	You're an AI concierge at Coral Cloud Resorts. Your role is to assist customers with booking and managing services during the film festival by providing accurate information and resolving inquiries swiftly.Copiar
Company	Coral Cloud Resorts offers destination experiences that blend unique, premium activities with unmatched customer care. Our discerning customers value effortless, quality reservation services, where every interaction enhances their journey.Copiar
Integrate Knowledge Articles in Agentforce Builder
To integrate Knowledge articles into Agentforce Builder and ensure the agent is grounded in relevant information, start by managing data sources to provide access to these articles. Create a data library named Coral Cloud Experience Agent LibraryCopiar, including the identifying fields Title and Summary and the content fields Answer and Question. While we won’t evaluate this configuration as part of the challenge, it's essential for grounding the agent in accurate knowledge from relevant articles.

Integrate the Code of Conduct and User Agreement File
Now, create a new data library with the name Code of Conduct AgreementCopiar and API name Code_of_Conduct_AgreementCopiar and upload the resort’s Code of Conduct and User Agreement. Tip: Don't rename the file; it should be named CC_User_Agreement.pdf. This resource grounds the agent’s responses in trusted and compliant data.

Note: Since a data library can only have one data type, you need two data libraries: one for Knowledge articles and another to upload the file.

Ensure the agent’s role, description, and company context reflect Coral Cloud Resorts’s mission and services. Confirm the Coral Cloud Experience Agent is linked to the Knowledge data library. Confirm that the Code of Conduct is uploaded to the data library. We use these two data sources in challenge 3.

Create the Booking Management Topic
The Coral Cloud Experience Agent must manage all booking-related interactions efficiently. To achieve this, configure the Booking Management Topic as follows.

Booking Management Topic and Agent Actions
Include a clear description, defined scope, and specific instructions for handling guest bookings. Ensure the topic is aligned with the resort’s commitment to seamless guest service.

Field	Value
Topic Label	Booking ManagementCopiar
Classification Description	This topic handles customer inquiries about booking experiences at Coral Cloud Resorts. It includes making new reservations, modifying existing bookings, and addressing questions about experience details to ensure a smooth and satisfying customer journey.Copiar
Scope	Your job is to assist customers with managing their bookings for Coral Cloud Resorts experiences. This includes providing accurate information, resolving booking-related issues, and ensuring every interaction is seamless and stress-free.Copiar
1st Instruction	Always request the Booking Record Number, which begins with 'B-', before accessing booking details. Use the 'Get Booking' action to retrieve and share the relevant information with the customer. Copiar
2nd Instruction	Prompt the user to specify the action they’d like to take on their booking. Available options include adding and removing guests or canceling the booking.Copiar
3rd Instruction	For booking cancellations, confirm the action with the user by displaying the Experience Name. Then call the 'Cancel Booking' action.Copiar
4th Instruction	To add guests to a confirmed booking, ask the user for the total number of guests, including the contact, who plan to attend the session. Use the previously provided Booking Record Number (starting with 'B-') to call the 'Adjust Booking' action.Copiar
Now that you have the instructions in place, you'll add actions to support booking modifications using the Adjust Booking flow, cancellations using the Cancel Booking flow, and information retrieval using the Get Booking flow. Ensure actions prompt for required inputs, such as the Booking Record Number, and display outputs correctly.

Tip: Take a look at the booking records in the Coral Cloud Resorts app before writing agent action instructions.

The agent should retrieve and share relevant booking information with the customer. Review the second instruction, which involves prompting the user to specify the action they’d like to take, such as adding guests or canceling a booking. Create the following actions in Agentforce Builder and add them to the Booking Management topic.

Get Booking
Adjust Booking
Cancel Booking
Configure the Cancel Booking action so that the agent confirms with the user before canceling the booking. Add additional instructions to the Booking Management topic to call the previous agent actions.

Note: We're not checking the loading text and input/output configurations of the agent actions beyond what's outlined above.

Ensure the Booking Management topic includes the correct classification description, scope, and instructions as specified, and the associated required agent actions. Test the agent with booking scenarios to ensure it correctly prompts, processes, and displays booking actions and details.


Note
When implementing record changes via AI, it’s best practice to include security measures such as user identity verification. This step is not required for this challenge but is encouraged for real-world scenarios. See Maintain Trust with Agentforce Actions for more information.

Add Standard Topics: General FAQ and Escalation
Coral Cloud Resorts needs its virtual concierge to deliver precise information about event details, policies, and other queries. Your task is to ensure the agent uses trusted data sources, such as Knowledge articles and the Code of Conduct PDF, for accurate responses. Additionally, you ensure the agent can escalate complex queries to a service representative when necessary. In this challenge, you'll configure standard topics and integrate data library retrievers for trusted data sources.

To complete this challenge, configure the Coral Cloud Experience Agent to meet the following needs.

Add the standard General FAQ Topic and customize it: Use an agent action to invoke the Film_Festival_Related_Answers prompt template. The prompt template generates a response to the user’s question based on the relevant information from Knowledge articles and the Code of Conduct file.
Add the Escalation Topic: Enable the agent to transfer unresolved inquiries to a service representative.
Review the prompt in the Film_Festival_Related_Answers prompt template and add the user’s question Input: Question in the placeholder text: [Input the customer's question].

Add Retrievers (which will have names similar to File_Code_of_Conduct... and KA_Coral_Cloud_Experience...) in the placeholder text indicated with brackets. Additionally, configure the Search Text for both the retrievers with the user input, Input: QuestionCopiar . Save, test, and activate the prompt template.

Tip: If you can't get the expected response from the prompt template, make sure you've rebuilt the search index for the Knowledge articles. See the Help article for detailed steps on how to rebuild the search index.

Set the guardrails to get answers from the response of the Film_Festival_Related_Answers prompt template. Create a new action to invoke the prompt template. Associate this new action to the General FAQ topic. Make sure there's only one General FAQ topic, and that it is customized with the new action.

Confirm the General FAQ topic overrides to call the new action. Ensure it retrieves results from the Knowledge articles and Code of Conduct sources. Check that responses are formatted appropriately for customer chats. Ensure that the associated action is configured correctly.

Lastly, verify that the agent is configured to escalate conversations to a live representative.

Deploy Agent and Transfer Conversations
Coral Cloud Resorts wants to add the Messaging service channel to its Experience Cloud site so guests can interact with the Coral Cloud Experience Agent. To ensure an exceptional guest experience, the resort needs you to configure the agent on the coral-cloud site. The setup must allow the guest to interact with the agent in the Experience Cloud site. This includes ensuring the necessary flows are set up, publishing updates, and activating all required components.

Confirm that the agent is activated and updated with the latest configurations. To transfer conversation from guests on the site to the Coral Cloud Experience Agent, the resort needs you to configure the inbound omnichannel flow, Route to ESA. Save and activate the updated flow.

In situations where the guests require assistance from a service representative, the org is equipped with the outbound omnichannel flow, ESA - Route to Queue. The Coral Cloud Experience Agent uses this flow to route escalations to a Messaging queue. Optionally include a message to inform guests about the transfer of the conversation to a service representative.

Note: Before adding the Embedded Messaging component to the coral-cloud Experience Cloud site, make sure you publish the site and the ESA Web Deployment embedded service. We're not checking this in the challenge, but it's critical to complete these steps before testing the agent with the site.

¿Listo para superar esta Superbadge?
Realizará el trabajo para esta Superbadge en su propia organización de prácticas. Cada Superbadge tiene requisitos, configuraciones, licencias y restricciones de organización exclusivos. Siga los pasos de la sección Trabajo previo y Notas cuidadosamente para configurar una nueva organización para esta Superbadge; esto podría implicar instalar un paquete en un nuevo Trailhead Playground o registrarse para una organización de Developer Edition especial.

Para trabajar con su Trailhead Playground, haga clic en Launch (Iniciar). Para crear una organización de Developer Edition especial, siga los pasos descritos en Prework (Trabajo previo) y Notes (Notas).

Seleccionar la organización de prácticas

epic.230a1774394155665@orgfarm.salesforce.com
Creada el 24/3/2026
Complete each challenge to earn your superbadge
1
Set Up the Agent and Einstein Data Library
Configure the Coral Cloud Experience Agent and create Agentforce Data Libraries as data sources for the agent. 



For more guidance, refer to the Help article.

2
Create the Booking Management Topic
Configure a custom topic to manage bookings by launching the flows: Get Booking, Adjust Booking, and Cancel Booking.



For more guidance, refer to the Help article.

3
Add Standard Topics
Modify the provided prompt with the data source retrievers. Override the General FAQ topic with a custom action to the prompt template. Configure the agent to be able to escalate conversations to a service representative. 



For more guidance, refer to the Help article.

4
Deploy Agent and Transfer Conversations
Adjust the Route to ESA flow to successfully deploy the Coral Cloud Experience Agent on the Experience Cloud site.



For more guidance, refer to the Help article.
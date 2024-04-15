<p>
<h1> ToDoList </h1>
A ToDoList project maded with using python and tkinter with firebase implimentation
</p>
<p>
<h1>How To Use : </h1>
Change : ('path/to/serviceAccountKey.json')
to the saved firebase .json file address
</p>
<p>
  <h2>Here's how you can obtain the service account key file: </h2>
  Go to the Firebase Console (https://console.firebase.google.com/).<br>
Select your project.<br>
Navigate to Project settings.<br>
In the Service accounts tab, click on the "Generate new private key" button.<br>
Save the JSON file that contains your service account key to your local machine.<br>
</p>
<p>
  <h3>Known Error and Its Solution : </h3>
  <h4>Error</h4>
  Error saving task: 403 Cloud Firestore API has not been used in project indigo-charge-414911 before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/firestore.googleapis.com/overview?project=indigo-charge-414911 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry. [links {
  description: "Google developers console API activation"
  <h4>Solution : </h4>
  The error message indicates that the Cloud Firestore API has not been enabled for your Firebase project or it is disabled. To rectify this issue, you need to enable the Cloud Firestore API for your project in the Google Cloud Console.
  <h4>Method To Solve : </h4>
<br>  Go to the Google Cloud Console: https://console.cloud.google.com/
<br>Select your project (in this case, "indigo-charge-414911").
<br>In the left sidebar menu, navigate to "APIs & Services" > "Dashboard".
<br>Click on the "+ ENABLE APIS AND SERVICES" button.
<br>In the search bar, type "Firestore".
<br>Select "Cloud Firestore API" from the search results.
<br>Click on the "ENABLE" button to enable the API.
</p>

This project comprises of both the tasks assigned

Task1:
1. Take Image and Xml File using React Frontend and Send it to Flask Backend
2. In the backend, the image gets processed and the image name and object names aren
stored in sqlite database.
3. The processed image is then sent back to React frontend for display

Task 2:
As per the start date and end date provided on UI
the data from the backend server is sent back.


Setup: (the following steps and commands are to be followed in windows)
1. Clone the repository
2. Through the terminal/cli
3. Navigate to api folder and activate a virtual environment 
4. To activate a virtual environment enter command "python -m venv venv" followed by "venv\Scripts\activate"
5. Install flask by running the commmand "pip install flask"
6. Install all the dependencies run the commmand "pip install -r requirements1.txt"
7. Now split the terminal and activate the environement by running the command "venv\Script\activate" if it is not in the environment mode
8. Install all the dependencies run the commmand "npm install -r requirements2.txt" if it gives error then manually install all the requirements listed in the txt file by running the command "npm install fask" and so on..
9. In previous terminal window navigate to api folder and Start backend server using command "npm run start-flask-api" if there is an error run the command "pip install python-dotenv" and then run "npm run start-flask-api"
10. In second terminal after navigating to app folder, on the terminal give command "npm start"



### output of Page :

![frontend image](https://user-images.githubusercontent.com/75617171/112715865-f18d1f00-8f08-11eb-8ddc-af80df676ef1.PNG)

### output of Task 1:

![Task1output](https://user-images.githubusercontent.com/75617171/112715872-f94cc380-8f08-11eb-9f47-bade0348c10d.PNG)

### output of Task 2:

![csv generated photo](https://user-images.githubusercontent.com/75617171/112715980-b0493f00-8f09-11eb-8d4e-18a6418841c8.PNG)


# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `yarn build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

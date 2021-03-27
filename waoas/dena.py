
'''import React , {useState, useEffect, Component, classe}from 'react';
import { Form, Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import logo from './logo.svg';
import './App.css';
import useFormData from 'react-use-form-data'
import axios from 'axios';

class App extends Component{
const [initialData, setinitialData] = useState([{}])
  state = {
    title: '',
  image : null,
  xml : null
  };

handleImageChange = (e) => {
  this.setState({
    image : e.target.files[0]
  })
};
handleXmlChange = (e) => {
  this.setState({
    xml : e.target.files[0]
  })
};

handleUploadImage = (e) => {
  e.preventDefault();
  //console.log(this.state)
  let fd = new useFormData();
  fd.append('image', this.state.image, this.state.image.name);
  fd.append('XMLFILE', this.state.xml, this.state.xml.name);

  /*axios.get('/api').then((response) => {
            console.log(response);
        })
    .catch((error) => {
        console.log(error);
    });*/
    fetch('/api').then(
        response => response.json()
      ).then(data =>console.log(data))
};

  render() {
    return (
      <div className="App">
      <form onSubmit = {this.handleSubmit}>
      <p>UploadImage</p>
      <div>
      <input type="file"
      id = "image" accept="image/png, image/jpeg"
       onChange={this.handleImageChange} required />
      </div>
      <div>
      <br/>
      <p>Upload xml file</p>
      <input type="file" id ="xml"
      onChange={this.handleXmlChange} required/>
      </div>
      <br />
      <div>
      <input type="submit" />
      </div>
      <img src={this.state.wapasImg} alt="img" />
      </form>
      </div>
    );
  }
}

export default App'''



import React , {useState, useEffect, Component, classe}from 'react';
import './App.css';
import axios from 'axios';
/*function App() {
  const [initialData, setinitialData] = useState([{}])*/

  class App extends Component{
  //const [initialData, setinitialData] = useState([{}])
  useEffect(() => {
    fetch('/api').then(
      response => response.json()
    ).then(data => console.log(data))
  /*  axios.post('/api').then((response) => {
               console.log(response);
           })
       .catch((error) => {
           console.log(error);
       });*/
  }

);
  /*return (
    <div className="App">
    <h1>{initialData.pooja}</h1>
    </div>
  );*/
  render() {
    return (
      <div className="App">
      <form onSubmit = {this.handleSubmit}>
      <p>UploadImage</p>
      <div>
      <input type="file"
      id = "image" accept="image/png, image/jpeg"
       onChange={this.handleImageChange} required />
      </div>
      <div>
      <br/>
      <p>Upload xml file</p>
      <input type="file" id ="xml"
      onChange={this.handleXmlChange} required/>
      </div>
      <br />
      <div>
      <input type="submit" />
      </div>
      <img src={this.state.wapasImg} alt="img" />
      </form>
      </div>
    );
  }
}

export default App;

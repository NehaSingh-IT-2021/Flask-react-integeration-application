
import React , {useState, useEffect, Component, classe}from 'react';
import { Form, Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import logo from './logo.svg';
import './App.css';
import useFormData from 'react-use-form-data'
import axios from 'axios';
import {CSVLink, CSVDownload} from 'react-csv';

class App extends Component{
//const [initialData, setinitialData] = useState([{}])

  state = {
  title: '',
  image : null,
  xml : null,
  wapasImg: null,
  startdate: '',
  enddate: '',
  csvfile : ''
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

handleChangeStart = (e) => {
  this.setState({
    startdate: e.target.value
  })
};

handleChangeEnd = (e) => {
  this.setState({
    enddate: e.target.value
  })
};

handleSubmit = (e) => {
  e.preventDefault();
  const fd = new FormData();
  fd.append('image', this.state.image, this.state.image.name);
  fd.append('XMLFILE', this.state.xml, this.state.xml.name);
  console.log(this.state)
  axios.post('/api',fd,{
      headers: {
        'content-type': 'multipart/form-data'
      }
    }).then((response) => /*console.log(response)*/{
      this.setState({
        wapasImg : 'data:image/png;base64,'
        +response.data['status'].split('\'')[1]
      })
    })
    .catch((error) => {
        console.log(error);
    });
};

handleSubmitCSV = (e) => {
  e.preventDefault();
  const user = {
    startdate : this.state.startdate,
    enddate : this.state.enddate
  }
  console.log(this.state)
  axios.post('/savetoCSV', { user })
  .then((res) => {
    console.log(''+res.data+'')
    this.setState({
      csvfile : ''+res.data+''
    })
  })
}

  render() {
    const data = this.state.awsApiData;
    return (
      <div className="App">
      <h1>TASK 1</h1>
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
      <input type="file" id ="xml" accept="txt/xml"
      onChange={this.handleXmlChange} required/>
      </div>
      <br />
      <div>
      <input type="submit" />
      </div>
      <img src={this.state.wapasImg} alt="img" />
      </form>
      <br/>
      <h1>TASK 2</h1>
      <form onSubmit = {this.handleSubmitCSV}>
      <label htmlFor="start">Start date:</label>
      <input type="date" id="start" value = {this.state.startdate} onChange={this.handleChangeStart} required/>
      <label htmlFor="end">End date:</label>
      <input type="date" id="end" value = {this.state.enddate} onChange={this.handleChangeEnd} required/>
      <input type="submit" />
      <br/>
      <br/>
      <br/>

      <CSVLink data = {this.state.csvfile}>Download CSV</CSVLink>

      </form>
      </div>
    );
  }
}

export default App

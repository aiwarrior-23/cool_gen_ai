import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Navbar, Nav } from 'react-bootstrap';
import Sidebar from './components/Sidebar';
import MainScreen from './components/MainScreen';
import './App.css';

function App() {
  return (
    <div className="App">
      <Navbar bg="dark" variant="dark" expand="lg" style={{paddingLeft:'1rem', textAlign:'center'}}>
        <Navbar.Brand href="#">Article Generator</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
      </Navbar>
      <Container fluid>
        <div className="d-flex">
          <Sidebar />
          <MainScreen />
        </div>
      </Container>
    </div>
  );
}

export default App;
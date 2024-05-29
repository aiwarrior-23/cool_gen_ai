import React from 'react';
import { Nav } from 'react-bootstrap';
import './Sidebar.css';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <Nav defaultActiveKey="/home" className="flex-column">
        <Nav.Link href="#home">Generate Article</Nav.Link>
      </Nav>
    </div>
  );
};

export default Sidebar;

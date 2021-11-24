import React from "react";
import { Link } from "react-router-dom";
import "./styles.css";
import note from "./icons/Icon.png";
import start from "./icons/Icon-1.png";
import ativity from "./icons/Icon-2.png";
import analysis from "./icons/Icon-3.png";

export default class Sidebar extends React.Component {
  render() {
    return (
      <div className="sidebar-component">
        <h3 className="sidebar-title">Natuur</h3>
        <div className="sidebar-items">
          <Link to="/nota" className="sidebar-element">
            <img src={note} alt="note icon" />
            <text>Nova nota</text>
          </Link>

          <Link to="/" className="sidebar-element">
            <img src={start} alt="start icon" />
            <text>Início</text>
          </Link>

          <Link to="/actividade" className="sidebar-element">
            <img src={ativity} alt="Ativity icon" />
            <text>Atividade</text>
          </Link>

          <Link to="/analise" className="sidebar-element">
            <img src={analysis} alt="Analysis icon" />
            <text>Análises</text>
          </Link>
        </div>
      </div>
    );
  }
}

import React from "react";
import { Card } from "./components/Card";
import { Header } from "./components/Header";
import { Footer } from "./components/Footer";

function App() {
  return (
    <React.Fragment>
    <div>
      <Header/>
      Hello word
      <Card 
        id={1}
        paragraph="Typescript"
        details="TS para frontend e backend"
      />
      <Card 
        id={2}
        paragraph="HTML" 
        details="HTML para frontend"
      />
      <Card 
        id={3}
        paragraph="SQL" 
        details="SQL para bancos de dados"
      />
    </div>
    <Footer/>
    </React.Fragment>
  );
}

export default App;

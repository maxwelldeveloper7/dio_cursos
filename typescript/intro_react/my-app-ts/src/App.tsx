import { Card } from "./components/Card";
import { Layout } from "./components/Layout";

function App() {
  return (
    <Layout>
      Hello world
      <Card
        id={1}
        paragraph="Typescript"
        details="Typescript para frontend e backend"
      />
      <Card
        id={2}
        paragraph="HTML"
        details="HTML para frontend e backend"
      />
      <Card
        id={1}
        paragraph="SQL"
        details="SQL para bancos de dados"
      />
    </Layout>
  );
}

export default App;

import { useState } from "react";
import { Box, ChakraProvider } from "@chakra-ui/react";
import { Card } from "./components/Card";
import { Layout } from "./components/Layout";

function App() {
  const [value, setValue] = useState(0);
  const [outroValor, setOutroValor] = useState(1)
  return (
    <ChakraProvider>
      <Layout>
        <Box minHeight="100vh" backgroundColor="#9413dc" padding="25px">
          <Card />
          <div>
            <button onClick={()=> setValue(value + 1)}>Add</button>
            <h1>{value}</h1>
          </div>
            <button onClick={()=> setOutroValor(outroValor + 1)}>Add</button>
            <h1>{outroValor}</h1>          
        </Box>
      </Layout>
    </ChakraProvider>
  );
}

export default App;

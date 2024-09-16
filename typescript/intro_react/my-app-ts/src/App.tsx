
import { Box, Button, Center, ChakraProvider, Input } from "@chakra-ui/react";
import { login } from "./services/login";

function App() {
  return (
    <ChakraProvider>
      <Box minHeight='100vh' backgroundColor='#9413dc' padding='25px' display='fex' flexDirection='row' justifyContent='center'>
        <Box backgroundColor='#ffffff' borderRadius='25px' padding='20px' width='50vw' height='25vh'>
        <Center margin='10px 5px'>
          <h1>Faça o login</h1>      
        </Center>
        <Input placeholder="email" margin='10px 0'/>
        <Input placeholder="password" margin='10px 0'/>
        <Center>
        <Button  onClick={login} colorScheme="teal" size='sm' width='100%' margin='10px 0'>
          Button
        </Button>
        </Center>
        </Box>
      </Box>    
    </ChakraProvider>
  );
}

export default App;

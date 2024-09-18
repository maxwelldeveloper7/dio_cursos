import { 
  Center,
  Input,
  Box,
  Heading
} from '@chakra-ui/react'
import { login } from '../services/login';
import { Header } from './Header';
import { Botao } from './Button';

export const Card = () => {
  return(
    
      <Box minHeight='100vh' backgroundColor='#9413dc' padding='25px'>        
        <Box backgroundColor='#FFFFFF' borderRadius='25px' padding='15px' >
          <Center>
            <Heading as="h2" size="md">Faça o login</Heading>
          </Center>
          <Input placeholder="email" margin="10px 0 10px 0"/>
          <Input placeholder="password" margin="0 0 10px 0" />
          <Center>
            <Botao onClick={login} />
          </Center>
        </Box>
      </Box>
  )
}

export default Card;
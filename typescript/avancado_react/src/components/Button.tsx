import { Button } from "@chakra-ui/react";

interface Botao{
    event:() => {};
}

export const Botao = ({ onClick }: { onClick:()=> void }) => {
  return(
    <Button colorScheme="teal" onClick={onClick} size='sm' width='100%' marginTop='5px'>Entrar</Button>
  )
};

export default Botao;
import { Box, Flex, Heading, Image } from "@chakra-ui/react";
import dio from './dio.svg'

export const Header = () => {
  return (
    <Box as="header" bg="orange" py={4} px={8} shadow="md">
      <Flex align="center">
        <Image 
          src={dio} boxSize="70px"
        />
        <Heading as="h1" size="lg" color="white">
          Bank
        </Heading>
      </Flex>
    </Box>
  );
};

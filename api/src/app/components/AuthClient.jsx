"use client";

import { useState } from 'react';
import { Inter } from 'next/font/google'
import { ApolloClient, ApolloProvider, InMemoryCache, createHttpLink } from '@apollo/client';
import { setContext } from "@apollo/client/link/context";
import { useAuth0 } from '@auth0/auth0-react';
import ApiCallExample from './ApiCallExample';

const inter = Inter({ subsets: ['latin'] })

const httpLink = createHttpLink({
  uri: 'http://localhost:8080/v1/graphql',
});

const authLink = setContext(() => {
  return {
    headers: {
      "x-hasura-admin-secret": "mylongsecretkey",
    }
  }
});

const createApolloClient = () => {
  return new ApolloClient({
    link: authLink.concat(httpLink),
    cache: new InMemoryCache(),
  })
};
    
const AuthClient = ({ children }) => {
  const { loading, logout } = useAuth0();
  if (loading) {
    <div>Loading...</div>
  }

  const [apolloClient] = useState(createApolloClient());

  return (
    <ApolloProvider client={apolloClient}>
      <ApiCallExample/>
    </ApolloProvider>
  )
}

export default AuthClient;
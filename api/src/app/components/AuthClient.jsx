"use client";

import { useState } from 'react';
import { Inter } from 'next/font/google'
import { ApolloClient, ApolloProvider, InMemoryCache, HttpLink } from '@apollo/client';
import { useAuth0 } from '@auth0/auth0-react';

const inter = Inter({ subsets: ['latin'] })

const idToken = 'X-Hasura-Admin-Secret: mylongsecretkey';

const createApolloClient = () => {
  return new ApolloClient({
    link: new HttpLink({
      uri: 'http://localhost:8080/v1/graphql',
    }),
    cache: new InMemoryCache(),
  });
 };

const AuthClient = ({ children }) => {
  const { loading, logout } = useAuth0();
  if (loading) {
    <div>Loading...</div>
  }

  const [apolloClient] = useState(createApolloClient(idToken));

  return (
    <ApolloProvider client={apolloClient}>
      <body className={inter.className}>{children}</body>
    </ApolloProvider>
  )
}

export default AuthClient;
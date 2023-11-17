"use client";
import React from "react";
import { useQuery } from "@apollo/client";
import { GET_TURBDITY } from "../queries/gqlQueries"

const ApiCallExample = () => {
    const { loading, error, data } = useQuery(GET_TURBDITY);
  
    if (loading) {
      return <div>Loading...</div>;
    }
    if (error) {
      console.error(error);
      return <div>Error!</div>;
    }
    return console.log(data);
  };
 
export default ApiCallExample;
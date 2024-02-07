"use client";
import React from "react";
import { useQuery } from "@apollo/client";
import { GET_INTERSECTION } from "../queries/gqlQueries"

const ApiCallExample = () => {
    const { loading, error, data } = useQuery(GET_INTERSECTION, { //set which query to run here with variables
      variables:  { point: { type: "Point", coordinates: [10.62, 59.65] }},
    });
  
    if (loading) {
      return <div>Loading...</div>;
    }
    if (error) {
      console.error(error);
      return <div>Error!</div>;
    }
    console.log(data);
    return (
      <div>
        <pre>{JSON.stringify(data, null, 2)}</pre>
      </div>
    );
  };
 
export default ApiCallExample;
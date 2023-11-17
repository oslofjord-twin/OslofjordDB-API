import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';

const typeDefs = `#graphql
  type Query {
    salinitys(RecordTime: String): Salinity
    turbiditys(RecordTime: String): Turbidity
  }
  type Salinity {
    RecordTime: String,
    RecordNumber: String,
    SensorStatus: String,
    Conductivity: String,
    Temperature: String
  }
  type Turbidity {
    RecordTime: String!,
    RecordNumber: String,
    SensorStatus: String,
    Turbidity: String,
    Temperature: String,
    TXCAmp: String,
    C1Amp: String,
    C2Amp: String,
    RawTemp: String
  }
`;

// Example values:
const salinitys = [
    {
        RecordTime: "2023-04-12 15:42:57",
        RecordNumber: "1178640",
        SensorStatus: "(0) OK",
        Conductivity: "3.573199E+01",
        Temperature: "7.607697E+00"
    },
    {
        RecordTime: "2023-04-12 15:42:58",
        RecordNumber: "1178641",
        SensorStatus: "(0) OK",
        Conductivity: "3.570759E+01",
        Temperature: "7.591591E+00"
    },
  ];

const resolvers = {
    Query: {
        salinitys(parent, args, contextValue, info) {
                return salinitys.find((Salinity) => Salinity.RecordTime === args.RecordTime);
         },
        turbiditys: () => turbiditys,
      },
  };

const server = new ApolloServer({ typeDefs, resolvers });

const { url } = await startStandaloneServer(server, {
    listen: { port: 4000 },
  });

console.log(`🚀  Server ready at: ${url}`);
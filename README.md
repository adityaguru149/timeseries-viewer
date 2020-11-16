# TimeSeries Viewer

## Run Locally

`docker-compose`

```bash
docker-compose up --build
```

## Design Decisions

- **Monorepo:** A mono-repo seemed suitable for this as there is need for sharing parts of the codebase across components (like `autogen` in grpc, `docker-compose.yml`). Moreover, this is a small project now and the setup effort can be kept lower this way. Every component has scope to have their own repositories.
- **gRPC:** Very high performance claims
- **REST:** Browser compatible
- **3 separate containers:** To be able to scale independently when requied.
- **pre built pandas container:** Pandas (+numpy) build was taking a long

## Challenges

- gRPC generated code has [issue](https://github.com/protocolbuffers/protobuf/issues/1491)
- gRPC documentation is difficult to find but [Docs](https://github.com/protocolbuffers/protobuf/tree/master/src/google/protobuf), [Github](https://googleapis.dev/python/protobuf/latest/) help a ton.
- react-datetime-picker seems to have a papercut bug with the clock.

## TODO

- Better Error handling and logs
- https://github.com/arqex/react-datetime/issues/753
- [Move React environment variables to runtime/loadtime configurable](https://www.freecodecamp.org/news/how-to-implement-runtime-environment-variables-with-create-react-app-docker-and-nginx-7f9d42a91d70/)
- Various aggregation levels (15min, 1hr, 1day, 5day, 1week, 1month)
- timezone support?
- Multiple files - belonging to different locations/countries. If location not provided, get aggregated?
- Support to add files
- CI/CD setup
- Performance Testing and Optimisations (like Dask?, react dynamic import?)
- React build performance

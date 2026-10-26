# Yoriito Vehicle API v0.2.0 Release Notes

**Platform Name:** Yoriito Vehicle API  
**Release Tag:** v0.2.0  
**Origin Release Tag:** v.0.1.0  
**Release Date:** 2026-10-26  

## **Overview**

Yoriito v0.2.0 introduces major enhancements across the Vehicle API, VSS, VISS, and Kura components. This release expands API and signal capabilities through support for COVESA VSS v6.0 such as Vehicle Motion Management definitions, and introduces Struct/StructArray support to improve consistency when handling related signals. It also aligns with the latest VSS specification by removing dedicated Availability node definitions and adopting standardized availability metadata. In addition, implementation quality has been improved through architectural refinements, enhanced error handling, resolution of layer violations, and performance improvements in Kura through an in-memory data broker architecture.

Quality and security processes have also been strengthened through enhanced CI/CD workflows, security scanning, fuzzing-based testing, and SBOM generation. Furthermore, integration testing has been separated from the Vehicle API repository into a dedicated integration-test repository, and tutorials and sample applications have been updated to reflect the latest capabilities and improve developer experience.

!!! tip "Highlights"
    **Added**  
    - COVESA VSS v6.0 support  
    - Struct and StructArray support  
    - Dedicated integration-test repository  
    - Enhanced CI/CD workflows, security scanning, fuzzing-based testing, and SBOM generation  
    **Improved**  
    - VSS specification compliance through standardized availability metadata  
    - Vehicle API architecture by resolving layer violation issues and enhancing error handling  
    - Kura performance through an in-memory data broker architecture  
    - Security through secure coding improvements  
    - Sample applications and tutorials  
    **Removed**  
    - Dedicated Availability node definition  
    - Integration repository  

### Limitations/Known Issues
- SCA and SBOM results for some C++ components are currently incomplete due to limitations in dependency analysis for Yocto-based build environments.
- Dynamic security testing coverage is currently limited because some DAST tool configurations are not yet fully implemented.
- Some cpplint findings related to header file include paths remain unresolved and will be addressed in a future release.

### Note
Please note that this is the preliminary release of the Yoriito Vehicle API towards v1.0.0, and as such, features are still under development. The software may become unstable or exhibit unexpected behavior, and there is a possibility of features/specification additions and breaking changes as development progresses.

## **Component Releases**
| Component | Release |
|-----------|---------------|
| yoriito | [v0.2.0](https://github.com/yoriito/yoriito/releases) |
| yoriito-vss | [v0.2.0](https://github.com/yoriito/yoriito-vss/releases) |
| yoriito-viss | [v0.2.0](https://github.com/yoriito/yoriito-viss/releases) |
| vehicle-api | [v0.2.0](https://github.com/yoriito/vehicle-api/releases) |
| integration-test | [v0.2.0](https://github.com/yoriito/integration-test/releases) |
| actions | [v0.2.0](https://github.com/yoriito/actions/releases) 
| meta-yoriito | [v0.2.0](https://github.com/yoriito/meta-yoriito/releases) |
| meta-yoriito-tutorial | [v0.2.0](https://github.com/yoriito/meta-yoriito-tutorial/releases) |
| yoriito-tutorial | [v0.2.0](https://github.com/yoriito/yoriito-tutorial/releases) |
| kura | [v0.2.0](https://github.com/yoriito/kura/releases) |

<!--
## Release Plan
xxx
-->

## **Contact Information**
If you have any questions, please open an issue on GitHub.
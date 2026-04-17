# Welcome to the Yoriito Project  
This GitHub organization hosts artifacts from the activities of the [JASPAR API standardization WG](https://www.jaspar.jp/english/activitiesWorkingGroups).  

## Introduction to the Yoriito Project  

For more information, please see the Yoriito [homepage](https://yoriito.dev).  

## Organization Repositories

| Repository | Description | Status |
|------------|-------------|--------|
| [yoriito](https://github.com/yoriito/yoriito) | Main repository for the Yoriito project | ✅ active  |

---

## Repositories for Yoriito Vehicle API Activity  

### Documents  

| Repository | Description | Status |
|------------|-------------|--------|
| [yoriito](https://github.com/yoriito/yoriito) | Repository for Yoriito Vehicle API documents, including release notes, tutorials, API reference guides, and Design Documentation | ✅ active  |

The deployed GitHub Pages site is available [here](https://docs.yoriito.dev).  

### Modules  

| Repository | Description | Status |
|------------|-------------|--------|
| [yoriito-vss](https://github.com/yoriito/yoriito-vss) | Repository for the Yoriito VSS | ✅ active |
| [yoriito-viss](https://github.com/yoriito/yoriito-viss) | Repository for the Yoriito VISS | ✅ active |
| [vehicle-api](https://github.com/yoriito/vehicle-api) | Repository for the Vehicle API and common libraries | ✅ active |

### Integrations  
| Repository | Description | Status |
|------------|-------------|--------|
| [integration](https://github.com/yoriito/integration) | Repository for the integration | ✅ active |

### Dev Infrastructure Toolkit  

| Repository | Description | Status |
|------------|-------------|--------|
| [actions](https://github.com/yoriito/actions)  | Repository for GitHub composite actions for CI/CD workflows | ✅ active |
| [meta-yoriito](https://github.com/yoriito/meta-yoriito) | Repository for the API development container, Yocto OS image, and Yocto SDK for the Vehicle API and related components | ✅ active |
| [meta-yoriito-tutorial](https://github.com/yoriito/meta-yoriito-tutorial) | Repository for the API development container, Yocto OS image, and Yocto SDK for sample applications used in the tutorials | ✅ active |

### References  

| Repository | Description | Status |
|------------|-------------|--------|
| [yoriito-tutorial](https://github.com/yoriito/yoriito-tutorial) | Repository for reference applications and reference PAL applications | ✅ active  |
| [kura](https://github.com/yoriito/kura) | Repository for reference implementations of the Yoriito VISS and PAL library | ✅ active |

### Quality Assessment  

The following tests have been performed. Please refer to the `quality` directory of the corresponding repositories for details.

| Category | vehicle-api | kura | yoriito-tutorial |
|----------|-------------| -----| -----------------|
| Unit Test | ✅ passed| ✅ passed | - |
| Integration Test | ✅ passed| - | - |
| Coding Style | ✅ passed| ✅ passed | - |
| Coding Metrics | ✅ passed| - | - |
| Static Analysis | ✅ passed| - | - |
| Dynamic Analysis | - | - | ✅ passed  |
| Performance | - | - | ✅ passed |

For SCA (Risk Analysis), SBOM, and startup check, please refer to the [quality assessment page](./quality/quality_assessment.md) of this repository.  

### Privacy Statement  

Please see the [Privacy Statement](./PRIVACY.md).
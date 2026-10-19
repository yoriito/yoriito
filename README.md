# Welcome to the Yoriito Project
This GitHub organization hosts artifacts from the activities of the [JASPAR API standardization WG](https://www.jaspar.jp/english/activitiesWorkingGroups).  
For an overview of the Yoriito project, please visit the [Yoriito Homepage](https://yoriito.dev).  

## Organization Repository
| Repository | Description | Status |
|------------|-------------|--------|
| [yoriito](https://github.com/yoriito/yoriito) | Main repository for the Yoriito project. This repository also includes release notes, tutorials, design documentation, and API reference guides of the Yoriito Vehicle API.| ✅ active  |

## Yoriito Vehicle API Activities
### Documents and Tutorials
The following documents are available on the [Yoriito Vehicle API Documentation](https://docs.yoriito.dev).
| Deployed Page | Description |  
|------------|-------------|  
| 📝 [Release Notes](https://docs.yoriito.dev/releasenotes/) | Version history, feature additions, bug fixes, and other changes |
| 🏗️ [Design Documentation](https://docs.yoriito.dev/design/) | Architecture overview |
| 📚 [API Reference](https://docs.yoriito.dev/apirefguide/) | Detailed API specifications for vehicle API and kura |
| 📖 [Tutorials](https://docs.yoriito.dev/tutorials/) | Guides for first-time users, application developers, and platform developers |

Documentation for previous versions: [v0.1.0](https://docs.yoriito.dev/backnumber-v0.1.0/)

### Repositories
#### Modules
| Repository | Description | Status |
|------------|-------------|--------|
| [yoriito-vss](https://github.com/yoriito/yoriito-vss) | Repository for the Yoriito VSS | ✅ active |
| [yoriito-viss](https://github.com/yoriito/yoriito-viss) | Repository for the Yoriito VISS | ✅ active |
| [vehicle-api](https://github.com/yoriito/vehicle-api) | Repository for the Vehicle API and common libraries | ✅ active |

#### Integration Tests
| Repository | Description | Status |
|------------|-------------|--------|
| [integration-test](https://github.com/yoriito/integration-test) | Repository for the integration tests | ✅ active |

#### Dev Infrastructure Toolkit
| Repository | Description | Status |
|------------|-------------|--------|
| [actions](https://github.com/yoriito/actions)  | Repository for GitHub composite actions for CI/CD workflows | ✅ active |
| [meta-yoriito](https://github.com/yoriito/meta-yoriito) | Repository for the API development container, Yocto OS image, and Yocto SDK for the Vehicle API and related components | ✅ active |
| [meta-yoriito-tutorial](https://github.com/yoriito/meta-yoriito-tutorial) | Repository for the API development container, Yocto OS image, and Yocto SDK for sample applications used in the tutorials | ✅ active |

#### References
| Repository | Description | Status |
|------------|-------------|--------|
| [yoriito-tutorial](https://github.com/yoriito/yoriito-tutorial) | Repository for reference applications and reference PAL applications | ✅ active  |
| [kura](https://github.com/yoriito/kura) | Repository for reference implementations of the Yoriito VISS and PAL library | ✅ active |

### Quality Assessment
The following tests have been performed. Please refer to the `quality` directory of the corresponding repositories for details.
| Category | [vehicle-api](https://github.com/yoriito/vehicle-api) | [kura](https://github.com/yoriito/kura) | [integration-test](https://github.com/yoriito/integration-test) | [yoriito-tutorial](https://github.com/yoriito/yoriito-tutorial) | 
|-------------------------|------------|------------|------------|------------|
| Unit Test               | ✅ pass | ✅ pass | - | - |
| SW Integration Test     | - | - | ✅ pass | - |
| Coding Style            | ⚠️ partial pass | ✅ pass | - | - |
| Coding Metrics          | ✅ pass | ✅ pass | - | - |
| Static Analysis (SAST)  | ✅ pass | ✅ pass | - | - |
| Dynamic Analysis (DAST) | ⚠️ partial pass | ⚠️ partial pass | - | ✅ pass |
| Risk Analysis (SCA)     | ❌ not pass | ⚠️ partial pass | - |- |
| SBOM                    | ❌ not pass | ⚠️ partial pass | - |- |
| Performance             | - | - | - | ✅ pass |
| Startup Check           | - | - | - | ✅ pass |

## Privacy Statement
Please see the [Privacy Statement](https://github.com/yoriito/yoriito/blob/main/PRIVACY.md).
// Generated contract sketch for cybou-core integration.
//
// This file is documentation, not compiled source.
// Suggested target: cybou-core/src/immunity/policy_bundle.rs

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ImmunityVerdict {
    Allow,
    Deny,
    NeedsApproval,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord)]
pub enum RiskLevel {
    Low,
    Medium,
    High,
    Critical,
}

#[derive(Debug, Clone)]
pub struct CompiledPolicyRule {
    pub id: String,
    pub verdict: ImmunityVerdict,
    pub risk: RiskLevel,
    pub reason: String,
}

#[derive(Debug, Clone)]
pub struct CommandPatternRule {
    pub id: String,
    pub regex: String,
    pub verdict: ImmunityVerdict,
    pub risk: RiskLevel,
    pub reason: String,
}

#[derive(Debug, Clone)]
pub struct ImmunityPolicyBundle {
    pub version: String,
    pub command_patterns: Vec<CommandPatternRule>,
    pub sensitive_targets: Vec<SensitiveTarget>,
}

#[derive(Debug, Clone)]
pub struct SensitiveTarget {
    pub id: String,
    pub pattern: String,
    pub verdict: ImmunityVerdict,
    pub risk: RiskLevel,
}

impl ImmunityPolicyBundle {
    pub fn evaluate_command(&self, command: &str) -> ImmunityVerdict {
        // Runtime implementation must use a safe regex engine and highest-risk match policy.
        // The LLM never decides this verdict.
        ImmunityVerdict::Allow
    }
}

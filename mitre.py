import json
import requests

# 1. Fetch official MITRE ATT&CK STIX 2.1 JSON
URL = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json"

print("Downloading the latest official MITRE ATT&CK STIX 2.1 database...")
res = requests.get(URL)
stix_data = res.json()

objects = stix_data.get("objects", [])

# Define Infrastructure Tactics and Platforms
INFRA_TACTICS = {"resource-development", "command-and-control"}
INFRA_PLATFORMS = {"IaaS", "Google Workspace", "Office 365", "Azure AD", "Containers", "Network"}

chunks = []

# Process all STIX objects
for obj in objects:
    obj_type = obj.get("type")
    
    # Skip deprecated or revoked items
    if obj.get("x_mitre_deprecated") or obj.get("revoked"):
        continue

    # 1. STIX Infrastructure Objects
    if obj_type == "infrastructure":
        name = obj.get("name", "Unknown Infrastructure")
        desc = obj.get("description", "No description available.")
        aliases = ", ".join(obj.get("aliases", []))
        
        doc = f"## [STIX-INFRA] {name}\n"
        if aliases:
            doc += f"**Aliases:** {aliases}\n"
        doc += f"### Description\n{desc}\n"
        chunks.append(doc)

    # 2. Attack Patterns (Techniques and Sub-techniques)
    elif obj_type == "attack-pattern":
        kill_chain = obj.get("kill_chain_phases", [])
        platforms = set(obj.get("x_mitre_platforms", []))
        
        # Check relevance to Infrastructure (by Tactic or Platform)
        is_infra_tactic = any(phase.get("phase_name") in INFRA_TACTICS for phase in kill_chain)
        is_infra_platform = bool(platforms.intersection(INFRA_PLATFORMS))
        
        if is_infra_tactic or is_infra_platform:
            # Extract ATT&CK ID
            ext_ids = [e["external_id"] for e in obj.get("external_references", []) if e.get("source_name") == "mitre-attack"]
            attack_id = ext_ids[0] if ext_ids else "N/A"
            
            name = obj.get("name", "")
            desc = obj.get("description", "No description available.")
            is_sub = obj.get("x_mitre_is_subtechnique", False)
            tactics_list = ", ".join([p.get("phase_name") for p in kill_chain])
            platform_str = ", ".join(platforms)
            
            # Format document in pure English
            doc = f"## [{attack_id}] {name}\n"
            doc += f"**Type:** {'Sub-technique' if is_sub else 'Main Technique'}\n"
            doc += f"**Tactics:** {tactics_list}\n"
            doc += f"**Platforms:** {platform_str}\n\n"
            doc += f"### Full Description\n{desc}\n"
            
            # Add Detection if available
            if "x_mitre_detection" in obj:
                doc += f"\n### Detection\n{obj['x_mitre_detection']}\n"
                
            chunks.append(doc)

# Save to File
output_file = "mitre_full_infrastructure_english.md"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n\n---\n\n".join(chunks))

print(f"Done! Saved {len(chunks)} infrastructure objects into '{output_file}'.")
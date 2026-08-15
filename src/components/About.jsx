import { profile, coreSkills } from "../data";

export default function About() {
  return (
    <section className="section" id="about">
      <h2>Sobre</h2>
      <p className="about__summary">{profile.summary}</p>

      <div className="chips">
        {coreSkills.map((skill) => (
          <span className="chip" key={skill}>
            {skill}
          </span>
        ))}
      </div>
    </section>
  );
}

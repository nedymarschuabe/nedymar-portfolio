import { profile } from "../data";
import profilePhoto from "../assets/profile.png";

export default function Hero() {
  return (
    <header className="hero">
      <img className="hero__avatar" src={profilePhoto} alt={profile.name} />

      <h1>{profile.name}</h1>
      <p className="hero__title">{profile.title}</p>
      <p className="hero__subtitle">{profile.subtitle}</p>

      <div className="hero__links">
        <a href={`mailto:${profile.email}`}>{profile.email}</a>
        <a href={`tel:+55${profile.phone.replace(/\D/g, "")}`}>{profile.phone}</a>
        <a href={profile.linkedin} target="_blank" rel="noreferrer">
          LinkedIn
        </a>
        <a href={profile.github} target="_blank" rel="noreferrer">
          GitHub
        </a>
      </div>
    </header>
  );
}
